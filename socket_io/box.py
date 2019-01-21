# -*- coding: utf-8 -*-
import eventlet
from eventlet.green import threading
from eventlet import sleep
from eventlet.green import socket
# from socket import IPPROTO_TCP, TCP_INFO, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_KEEPALIVE, SHUT_RDWR
from socket import IPPROTO_TCP, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_KEEPALIVE, SHUT_RDWR
from array import array
from struct import unpack, pack
import sys
from hashlib import md5
from base64 import b64encode
from datetime import datetime
# import rm_list
from json import dumps
# from esim import library, makePkg
import time
# from quat import qu
import os

def getBool(d):
    return True if d == 0xAA else False if d == 0x55 else None

class sock(object):
    def __init__(self, address = '192.168.0.108', port = 10000):
        self.sock = socket.socket(AF_INET, SOCK_STREAM)
        self.sock.settimeout(0.1)
        self.address = address
        self.port = port
        self.connected = False
        self.connect(10)

    def printerr(self, info):
        print("[ERROR] PORT:", self.port, info)

    def connect(self, limit):
        wait = 0
        while wait < limit:
            wait += 1
            try:
                self.sock.connect((self.address, self.port))
            except socket.timeout:
                self.printerr("Socket Timeout.")
                sleep(1.0)
            except socket.error:
                self.printerr("Connect Error.")
                sleep(1.0)
            else:
                print("PORT:", self.port, "Conected")
                sleep(0.1)

                self.connected = True
                break

    def recv(self, recvlen = 1024):
        try:
            string = self.sock.recv(recvlen)
        except socket.error:
            self.printerr("Recv Error.")
            return ""
        except socket.timeout:
            self.printerr("Recv Timeout.")
            return ""
        else:
            return string

    def recvArr(self, recvlen = 1024):
        string = self.recv(recvlen)
        if string:
            return unpack(len(string) * 'B', string)
        else:
            return []

    def sendAndRecv(self, data, recvlen = 1024):
        try:
            self.sock.send(array('B', data))
        except socket.error:
            self.printerr("Send Error.")
        except socket.timeout:
            self.printerr("Send Timeout.")
        else:
            if recvlen > 0:
                try:
                    string = self.sock.recv(recvlen)
                except socket.error:
                    self.printerr("Recv Error.")
                    return ""
                except socket.timeout:
                    self.printerr("Recv Timeout.")
                    return ""
                else:
                    return string

    def sendAndRecvArr(self, data, recvlen = 1024):
        string = self.sendAndRecv(data, recvlen)
        if string:
            return unpack(len(string) * 'B', string)
        else:
            return []


class ctrlsock(sock):
    def __init__(self, address = '192.168.0.108', port = 10000):
        super(ctrlsock, self).__init__(address, port)
        self.getconf()

    def getconf(self):
        while True:
            string = self.sendAndRecv([0xA5, 0x05, 0x00], 231)
            if not string:
                print("[ERROR] GET CONFIG FAILED, RETRY CONNECTION.")
                self.sock.shutdown(SHUT_RDWR)
                self.sock.close()
                sleep(1.0)
                self.sock = socket.socket(AF_INET, SOCK_STREAM)
                self.sock.settimeout(0.1)
                self.connect(1)
                sleep(0.1)
            elif len(string) == 231:
                if unpack(">H", string[0:2])[0] == 0x5A05:
                    self.strtStrt = getBool(unpack("B", string[5:6])[0])
                    self.esimStrt = getBool(unpack("B", string[6:7])[0])
                    self.aocsStrt = getBool(unpack("B", string[7:8])[0])
                    self.lvdsStrt = getBool(unpack("B", string[8:9])[0])
                    self.camlStrt = getBool(unpack("B", string[9:10])[0])
                    self.dspdStrt = getBool(unpack("B", string[10:11])[0])
                    self.powrStrt = getBool(unpack("B", string[11:12])[0])
                    self.etrStrt  = getBool(unpack("B", string[12:13])[0])

                    self.ctrlPORT = unpack("H", string[13:15])[0]
                    self.esimPORT = unpack("H", string[15:17])[0]
                    self.aocsPORT = unpack("H", string[17:19])[0]
                    self.lvdsPORT = unpack("H", string[19:21])[0]
                    self.camlPORT = unpack("H", string[21:23])[0]
                    self.dspdPORT = unpack("H", string[23:25])[0]
                    self.powrPORT = unpack("H", string[25:27])[0]
                    self.dynaPORT = unpack("H", string[27:29])[0]

                    self.ctrlAddr = unpack("4B", string[29:33])

                    self.esimMode = unpack("B", string[96:97])[0]
                    self.esimCOM  = unpack("B", string[106:107])[0]
                    self.esimDATB = unpack("B", string[107:108])[0]
                    self.esimBDRT = unpack("I", string[108:112])[0]
                    self.esimPRTY = unpack("B", string[112:113])[0]
                    self.esimSTOP = unpack("B", string[113:114])[0]

                    self.aocsConn = getBool(unpack("B", string[114:115])[0])
                    self.aocsAddr = unpack("4B", string[115:119])

                    self.aocsCOM  = unpack("B", string[133:134])[0]
                    self.aocsDATB = unpack("B", string[134:135])[0]
                    self.aocsBDRT = unpack("I", string[135:139])[0]
                    self.aocsPRTY = unpack("B", string[139:140])[0]
                    self.aocsSTOP = unpack("B", string[140:141])[0]

                    break
                else:
                    print("[ERROR] GET CONFIG HEAD ERROR.")
            else:
                print("[ERROR] GET CONFIG TOO SHORT.")


    def switchfunc(self, func, en):
        FUNCTBL = {'esim': 0x01, 'aocs': 0x02, 'lvds': 0x03, 'caml': 0x04, 'dspd': 0x05, 'powr': 0x06}
        try:
            code = FUNCTBL[func]
        except:
            code = 0
            self.printerr('Function Name Unfound.')
            return

        if en:
            string = self.sendAndRecv([0xA5, 0x02, code, 0xAA, 0x00], 5)
        else:
            string = self.sendAndRecv([0xA5, 0x02, code, 0x55, 0x00], 5)

        self.getconf()

    def setserconf(self, func, com = 'COMA', databits = 8, baudrate = 115200, parity = 'ODD', stopbits = 1):
        if func == 'aocs':
            code = [0x20]
        elif func == 'esim':
            code = [0x12, 0x01]
        COMTBL = {'COMA': 0, 'COMB': 1, 'COM1': 2, 'COM2': 3, 'COM3': 4, 'COM4': 5}
        PARITYTBL = {'NONE': 0, 'ODD': 1, 'EVEN': 2}

        com = COMTBL[com]
        parity = PARITYTBL[parity]
        baudrate = list(unpack('4B', pack('I', baudrate))) if baudrate != None else list(unpack('4B', pack('I', self.baudrate)))
        string = self.sendAndRecv([0xA5] + code + [com, databits] + baudrate +[parity, stopbits, 0x00], 5)
        print('SET AOCS SERIAL PARAM.')

class lvdssock(sock):
    def __init__(self, csock, address = '192.168.0.108', port = 10003):
        self.csock = csock
        self.csock.getconf()

        self.csock.switchfunc('lvds', True)
        print("LVDS FUNCTION ENABLE.")

        super(lvdssock, self).__init__(address, port)

    def recv(self):
        while True:
            sleep(0.01)
            try:
                string = self.sock.recv(4096)
            except:
                self.printerr("Recv Error.")
            else:
                print([hex(i) for i in unpack(len(string) * 'B', string)])




class aocssock(sock):
    def __init__(self, csock, address = '192.168.0.108', port = 10001, com = 'COMA', databits = 8, baudrate = 115200, parity = 'ODD', stopbits = 1):
        self.csock = csock
        self.com = com
        self.databits = databits
        self.baudrate = baudrate
        self.parity   = parity
        self.stopbits = stopbits
        self.recvFail = 0
        self.prod = None
        self.csock.getconf()
        # ETR START
        string = self.csock.sendAndRecv([0xA5, 0x07, 0xAA, 0xE8, 0x03, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00], 5)
        print(['%02X'%i for i in unpack('5B', string)])
        while self.csock.aocsStrt:
            self.csock.switchfunc('aocs', False)
            print("AOCS FUNCTION DISABLE.")
        self.csock.setserconf('aocs', com, databits, baudrate, parity, stopbits)
        while not self.csock.aocsStrt:
            self.csock.switchfunc('aocs', True)
            print("AOCS FUNCTION ENABLE.")

        super(aocssock, self).__init__(address, port)
        sleep(0.1)
        try:
            string = self.sock.recv(4096)
        except:
            pass
        sleep(0.1)
        self.GetProdInfo()

    def GetProdInfo(self):
        PRODTBL = {0: 'ST-CCD2-2B', 1: 'ST-CCD2-2BG', 2: 'ST-CCD3-2', 3: 'ST-APS2-2A'}
        string = self.sendAndRecvArr([0x74, 0xA6, 0xC9, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE3], 5)
        if string and len(string) == 5 and string[0] == 0x8A and string[1] == 0x90:
            print("Product", PRODTBL[string[2] >> 4])
            self.prod = PRODTBL[string[2] >> 4]

    def showParam(self):
        COMTBL = {0: 'COMA', 1: 'COMB', 2: 'COM1', 3: 'COM2', 4: 'COM3', 5: 'COM4'}
        PARITYTBL = {0: 'NONE', 1: 'ODD', 2: 'EVEN'}

        print('+-AOCS-PARAM-+------------+')
        print('| COM        |', "%10s" % COMTBL[self.csock.aocsCOM], '|')
        print('| DATABITS   |', "%10d" % self.csock.aocsDATB, '|')
        print('| BAUDRATE   |', "%10d" % self.csock.aocsBDRT, '|')
        print('| PARITY     |', "%10s" % PARITYTBL[self.csock.aocsPRTY], '|')
        print('| STOPBITS   |', "%10d" % self.csock.aocsSTOP, '|')
        print('+------------+------------+')

    def getRmPkg(self, pkg):
        RMTBL = {
            'pkg1' : {'cmd' : [0x74, 0xA1, 0x00, 0x00, 0x15], 'len' : 64,   'head' : 0x8AA10000},
            'pkg2' : {'cmd' : [0x74, 0xA1, 0x00, 0x05, 0x1A], 'len' : 256,  'head' : 0x8AA10005},
            'pkg3' : {'cmd' : [0x74, 0xA1, 0x00, 0x06, 0x1B], 'len' : 512,  'head' : 0x8AA10006},
            'pkg4' : {'cmd' : [0x74, 0xA1, 0x00, 0x09, 0x1E], 'len' : 64,   'head' : 0x8AA10009},
            'pkg5' : {'cmd' : [0x74, 0xA1, 0x00, 0x0A, 0x1F], 'len' : 128,  'head' : 0x8AA1000A}
        }
        string = self.sendAndRecv(RMTBL[pkg]['cmd'], RMTBL[pkg]['len'])
        if string and len(string) == RMTBL[pkg]['len']:
            if unpack('>I', string[0:4])[0] != RMTBL[pkg]['head']:
                self.recvFail += 1
                if self.recvFail > 30:
                    sleep(0.1)
                    try:
                        string = self.sock.recv(4096)
                    except:
                        pass
                    sleep(0.1)
                    self.recvFail = 0
                    print("[ERROR] FLUSH RECV BUFFER.")
                else:
                    print("[ERROR] RM HEAD ERROR.")
                return 'HEAD', ""
            if (sum(unpack(str(RMTBL[pkg]['len'] - 1) + 'B', string[0: -1])) & 0xFF) != unpack('B', string[-1:])[0]:
                print('[ERROR] RM CHECK SUM ERROR.')
                return 'CHKSUM', ""
            return 'OK', string
        else:
            print("[ERROR] NO RM PKG.")
            return 'NO', ""


class esimsock(sock):
    def __init__(self, csock, address = '192.168.0.108', port = 10000, com = 'COMB', databits = 8, baudrate = 115200, parity = 'ODD', stopbits = 1):
        self.csock = csock
        self.com = com
        self.databits = databits
        self.baudrate = baudrate
        self.parity   = parity
        self.stopbits = stopbits
        self.recvFail = 0
        self.prod = None
        self.count = 0
        self.library = library(os.path.dirname(__file__) + '/full_star_library.dat')
        self.csock.getconf()
        while self.csock.esimStrt:
            self.csock.switchfunc('esim', False)
            print("ESIM FUNCTION DISABLE.")
        self.csock.setserconf('esim', com, databits, baudrate, parity, stopbits)
        while not self.csock.esimStrt:
            self.csock.switchfunc('esim', True)
            print("ESIM FUNCTION ENABLE.")
        super(esimsock, self).__init__(address, port)

    def showParam(self):
        COMTBL = {0: 'COMA', 1: 'COMB', 2: 'COM1', 3: 'COM2', 4: 'COM3', 5: 'COM4'}
        PARITYTBL = {0: 'NONE', 1: 'ODD', 2: 'EVEN'}

        print('+-ESIM-PARAM-+------------+')
        print('| COM        |', "%10s" % COMTBL[self.csock.esimCOM], '|')
        print('| DATABITS   |', "%10d" % self.csock.esimDATB, '|')
        print('| BAUDRATE   |', "%10d" % self.csock.esimBDRT, '|')
        print('| PARITY     |', "%10s" % PARITYTBL[self.csock.esimPRTY], '|')
        print('| STOPBITS   |', "%10d" % self.csock.esimSTOP, '|')
        print('+------------+------------+')

    def sendEsimPkg(self, prod, qu, maxst = 20, utc = None):
        if not utc:
            utc = int((datetime.now() - datetime.strptime("2000 1 1 11:58:55.816","%Y %m %j %H:%M:%S.%f")).total_seconds() * 1000)
        esimpkg = makePkg(prod, qu, utc, maxst, self.count, self.library.stars)
        self.count += 1
        self.sendAndRecv(esimpkg, 0)


def GetMd5(pkg, string):
    if pkg == 'pkg1':
        return md5(b64encode(string[4: -1])).hexdigest()
    elif pkg == 'pkg2':
        return md5(b64encode(string[4: 45])).hexdigest()
    elif pkg == 'pkg3':
        return md5(b64encode(string[4: 61])).hexdigest()
    elif pkg == 'pkg4':
        return md5(b64encode(string[4: 33])).hexdigest()
    elif pkg == 'pkg5':
        return md5(b64encode(string[4: 63])).hexdigest()

class box(object):
    ctrl_port = 10000
    esim_port = 10001
    aocs_port = 10002
    lvds_port = 10003
    caml_port = 10004
    dspd_port = 10005
    powr_port = 10006
    dyna_port = 8000

    def __init__(self, address = '192.168.0.108'):
        self.address = address
        self.csock = ctrlsock(self.address, box.ctrl_port)
        self.pkgsel = ['pkg5', 'pkg4', 'pkg3', None]
        # self.pkgsel = []

        self.id = 0
        self.cmd = []
        self.cmdStat = False
        self.esimqu = qu([0, 10, 0])
        self.esimdec = 10.0
        self.esimroll = 0.0
        self.esimstep = 0.2
        self.esimopen = True
        self.esimmaxs = 20
        self.buf = {'pkg1': False, 'pkg2': False, 'pkg3': False, 'pkg4': False, 'pkg5': False}

    def initAocs(self, com = 'COMA', databits = 8, baudrate = 115200, parity = 'NONE', stopbits = 2):
        self.asock = aocssock(self.csock, self.address, box.aocs_port, com, databits, baudrate, parity, stopbits)

    def initLvds(self):
        self.lsock = lvdssock(self.csock, self.address, box.lvds_port)

    def initESim(self, com = 'COMB', databits = 8, baudrate = 115200, parity = 'ODD', stopbits = 1):
        self.esock = esimsock(self.csock, self.address, box.esim_port, com, databits, baudrate, parity, stopbits)
        self.esock.showParam()

    def addDat(self, pkg, string):
        rm_list.decodePkg(False, pkg, self.buf, string, prod = self.asock.prod)
        if pkg == 'pkg5':
            self.buf['pixel'] = rm_list.getPixel(string)
        if pkg == "pkg3":
            self.buf['clt'] = rm_list.getCltStars(self.buf['cltc'], string)
            self.buf['sts'] = rm_list.getRcgStars(self.buf['navc'], self.buf['rcgc'], string)
        if pkg == 'pkg2':
            self.buf['clt2'] = rm_list.getPkg2Stars(self.buf['rcgc'], string)
        if 'now' not in self.buf:
            self.buf['now'] = datetime.now().strftime('%Y%m%d %H.%M.%S.%f')[:-4]
        self.buf[pkg] = True


    def getRmPkg(self, pkg, curpkg = ""):
        stat, string = self.asock.getRmPkg(pkg)
        sleep(0.005)
        if (stat == "OK") and curpkg:
            chkpart = GetMd5(curpkg, string)
        else:
            chkpart = ""
        if (stat == "OK") and (pkg == "pkg1"):
            chkall = GetMd5('pkg1', string)
        else:
            chkall = ""
        return stat, string, chkpart, chkall

    def sendRmPkg(self, skio, cmdStat):
        rm_list.addCustom(False, self.buf)
        self.buf['cnt'] = self.id
        skio.emit("aocs", dumps(self.buf), namespace='/')
        self.cmdStat = cmdStat
        self.id += 1
        self.buf = {'pkg1': False, 'pkg2': False, 'pkg3': False, 'pkg4': False, 'pkg5': False}

    def handleCmd(self, skio):
        done = False
        while self.cmd:
            cmd = self.cmd.pop(0)
            if cmd['type'] == 'set':
                if cmd['name'] == 'setPkg':
                    self.pkgsel = cmd['value']
            elif cmd['type'] == 'time':
                t = int((datetime.now() - datetime.strptime("2000 1 1 11:58:55.816","%Y %m %j %H:%M:%S.%f")).total_seconds() * 1000)
                code = [0x74, 0xA3, (t >> 32) & 0xFF, (t >> 24) & 0xFF, (t >> 16) & 0xFF, (t >> 8) & 0xFF, (t >> 0) & 0xFF]
                self.asock.sendAndRecvArr(code + [sum(code) & 0xFF], 5)
            elif cmd['type'] == 'cmd':
                retPkg = {'value': self.asock.sendAndRecvArr(cmd['value'], cmd['retlen']), 'cmdcnt': cmd['name']}
                skio.emit("cmd", dumps(retPkg), namespace='/')
                print(retPkg)
                sleep(0.01)
            done = True
        return done

    def updateEsim(self, opene, step, dec, roll, maxs):
        self.esimdec  = float(dec)
        self.esimroll = float(roll)
        self.esimstep = float(step)
        self.esimopen = opene
        self.esimmaxs = int(maxs)

    def appendCmd(self, cmd):
        self.cmd.append(cmd)

    def esimStep(self):
        threading.Timer(0.1995, self.esimStep).start()
        if self.esimopen:
            self.esock.sendEsimPkg(self.asock.prod, self.esimqu, self.esimmaxs)
            self.esimqu = qu([self.esimqu.axis[0] + self.esimstep, self.esimdec, self.esimroll])

    def lvdsStep(self):
        self.lsock.recv()

    def aocsStep(self, skio):
        chkall = ""
        curPkg = ""
        chkpart = ""
        Flag1 = False
        FCnt = 0
        while True:
            cmdStat = self.handleCmd(skio)

            if not self.pkgsel:
                chkall_ = chkall
                stat, stringPkg1, chkpartPkg1, chkall = self.getRmPkg('pkg1', curPkg)
                if stat != "OK":
                    sleep(0.05)
                    continue
                if chkall != chkall_:
                    self.sendRmPkg(skio, cmdStat)
                    self.addDat('pkg1', stringPkg1)
                    FCnt = 0
                else:
                    FCnt += 1

                sleep(0.04)

                if FCnt > 10:
                    FCnt = 0
                    self.sendRmPkg(skio, cmdStat)
                    self.addDat('pkg1', stringPkg1)

            else:
                chkall_ = chkall
                stat, stringPkg1, chkpartPkg1, chkall = self.getRmPkg('pkg1', curPkg)
                if stat != "OK":
                    sleep(0.05)
                    continue

                if (chkall == chkall_) and (FCnt < 25):
                    FCnt += 1
                    continue
                else:
                    FCnt = 0


                if Flag1 and chkpartPkg1 == chkpart:
                    Flag1 = False
                else:
                    self.sendRmPkg(skio, cmdStat)

                self.addDat('pkg1', stringPkg1)

                tmpPkgs = [self.pkgsel.pop(0)]
                if self.pkgsel:
                    tmpPkgs.append(self.pkgsel.pop(0))
                self.pkgsel += tmpPkgs

                for curPkg in tmpPkgs:
                    if curPkg:
                        chkpartPkg1 = GetMd5(curPkg, stringPkg1)

                        stat, string, chkpart, null = self.getRmPkg(curPkg, curPkg)
                        if stat != "OK":
                            sleep(0.05)
                            continue
                        if chkpartPkg1 != chkpart:
                            self.sendRmPkg(skio, cmdStat)
                            self.addDat(curPkg, string)
                            Flag1 = True
                            break
                        else:
                            self.addDat(curPkg, string)


import socket

from struct import unpack, pack
from decode_lvds2 import decode_data, decode_data, rmStruct, rmTree
import eventlet
from eventlet.green import threading
from eventlet.green import socket
from eventlet import sleep
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from json import dumps, loads
import time


# ******** TCP connect *************
ip_port = ('192.168.0.90', 8990)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # udp协议 socket.SOCK_DGRAM
server.bind(ip_port)
server.listen(1)
tctimeClient, addr = server.accept()
###################################


# ******** flask ******************
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app, async_mode = 'eventlet')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getRmStr')
def get_rm_struct():
    return jsonify({"rmStruct": rmStruct})


@app.route('/getRmTree')
def get_rm_tree():
    return jsonify(rmTree)


@app.route('/getVal')
def get_data():
    return jsonify({'res': [x.as_dict() for x in db_rm_val.query.filter(db_rm_val.id < request.args.get("end")).filter(db_rm_val.id > request.args.get("start")).all()]})

@app.route('/getLastVal')
def get_lastest_data():
    print(request.args.get("src"))
    tar = request.args.get("src")
    if not tar:
        tar = package.pkg_src
    print(tar)
    if tar == 'aocs':
        return jsonify({'res': [x.as_dict() for x in db_rm_val.query.order_by(db_rm_val.id.desc()).limit(request.args.get("cnt")).all()]})
    elif tar == 'lvds':
        return jsonify({'res': [x.as_dict() for x in db_lv_val.query.order_by(db_lv_val.id.desc()).limit(request.args.get("cnt")).all()]})

class MyTask(object):
    def __init__(self):
        super(MyTask, self).__init__()
        self.open = False
        self.para = {}
    def update(self, para):
        self.open = para['open']
        self.para = para

class UpdTime(MyTask):
    def __init__(self):
        super(UpdTime, self).__init__()
        self.cnt = 0
    def step(self):
        self.cnt += 1
        if self.open and (self.cnt % int(self.para['period']) == 0):
          b.appendCmd({'type':'time'})

@sio.on('server')
def send_cmd(message):
    msg = loads(message)
    if msg['type'] == 'cmd':
        # b.appendCmd(msg)
        print(["0x%02X" % i for i in msg['value']])
        aceCmd.sendAndRecvArr(msg['value'], 0)
    # if msg['type'] == 'set':
    #     if msg['name'] == 'ETR':
    #         code = [0xA5, 0x07]
    #         code += [0xAA] if msg['code']['open'] else [0x55]
    #         code += unpack('4B', pack('I', int(msg['code']['period'])))
    #         code += unpack('4B', pack('I', int(msg['code']['width'])))
    #         code += [0x00]
    #         string = b.csock.sendAndRecv(code, 5)
    #         print ["%02X" % i for i in unpack("5B", string)]
    #     elif msg['name'] == 'TIME':
    #         updTime.update(msg['code'])
    #     elif msg['name'] == 'ESIM':
    #         print msg['code']
    #         b.updateEsim(msg['code']['open'], msg['code']['step'], msg['code']['dec'], msg['code']['roll'], msg['code']['maxstcnt'])


# ************************************************


def get_lvds():
    count = 0
    datastr = {}
    cnt = 0  # html view flag

    while True:

        head_info = tctimeClient.recv(16)
        # print('server head: ', head_info)
        if not head_info:
            break

        # startime = time.time()

        lvds_head = unpack("<I", head_info[0:4])
        print(hex(lvds_head[0]))
        if hex(lvds_head[0]) == "0x5555aaaa":
            print("package head RIGHT")
        else:
            raise Exception("package head ERROR")
        lvds_length = unpack("<I", head_info[4:8])[0]
        print("||received total length: || %s BYTE" % lvds_length)
        current_package_length = unpack("<I", head_info[8:12])[0]
        # print(hex(current_package_length))
        print("||current package length:|| %s BYTE" % current_package_length)
        package_total = unpack('<H', head_info[12:14])[0]
        # print(hex(package_total))
        print("||total package number:  || %s" % package_total)
        package_count = unpack('<H', head_info[14:16])[0]
        # print(hex(package_count))
        print("||current package count: || %s" % package_count)
        # print(type(package_count))

        datastr[package_count] = tctimeClient.recv(current_package_length)
        # print('server data: ', datastr)
        # print(len(datastr))

        count += len(datastr[package_count])
        print(count)

        if count == lvds_length:
            count = 0
            cnt += 1
            package = b''
            for i in range(package_total):
                package += datastr[i]

            data = package
            rm_buffer = {}

            frame_head_scp = unpack('>H', data[0:2])[0]
            if hex(frame_head_scp) == '0x8a5c':
                decode_data(rm_buffer, "CAK_TST_SCP", data[0:2048])
                data_CAK_TST_THR = data[2048: 4096]
                decode_data(rm_buffer, "CAK_TST_THR", data_CAK_TST_THR[0:2048])

            # data = data[4096:]
            # start = 0
            # end = 0
            # ncnt = 0
            # while start != '0x8a' or end != '0x5b':
            #     start = hex(data[ncnt])
            #     end = hex(data[ncnt + 1])
            #     ncnt += 2
            # decode_data(rm_buffer, "SUBWIN_DAT", data[ncnt - 2:])
            frame_head_win = unpack('>H', data[4096:4098])[0]
            if hex(frame_head_win) == '0x8a5b':
                win_info = unpack('>H', data[4098:4100])[0]
                win_num = ((win_info & (2 ** 12 - 1)) >> 8) + 1
                win_x = ((win_info & (2 ** 8 - 1)) >> 4) + 1
                win_y = (win_info & (2 ** 4 - 1)) + 1
                start = 4096 + 4
                rm_buffer['WIN_NUM'] = win_num
                rm_buffer['WIN_x'] = win_x
                rm_buffer['WIN_Y'] = win_y
                rm_buffer['PIXEL'] = []
                rm_buffer['SEG_Y'] = []
                rm_buffer['SEG_X'] = []
                rm_buffer['SEG_BKG'] = []
                rm_buffer['SEG_VLD_FLAG'] = []
                rm_buffer['SEG_ENER'] = []
                rm_buffer['SEG_WEIGHTED_ENER_LOW'] = []
                rm_buffer['SEG_LENGTH'] = []
                rm_buffer['SEG_WEIGHTED_ENER_HIGHT'] = []
                rm_buffer['PIXEL_FLAG'] = []
                rm_buffer['GS_ID'] = []
                rm_buffer['wrs'] = []
                rm_buffer['wcs'] = []
                for i in range(win_num):
                    decode_data(rm_buffer, "SUBWIN_DAT", data[start:])
                    rm_buffer['PIXEL'].append(rm_buffer['WIN1_PIXEL_VALUE'])
                    rm_buffer['PIXEL'] += [0, 0, 0]  # get a 256 dimension array
                    rm_buffer['PIXEL_FLAG'].append(rm_buffer['WIN1_PIXEL_OVER_FLAG'])
                    rm_buffer['PIXEL_FLAG'] += [0, 0, 0]
                    rm_buffer['SEG_Y'].append(rm_buffer['WIN1_SEG_Y'])
                    rm_buffer['SEG_X'].append(rm_buffer['WIN1_SEG_X'])
                    rm_buffer['SEG_BKG'].append(rm_buffer['WIN1_SEG_BKG'])
                    rm_buffer['SEG_VLD_FLAG'].append(rm_buffer['WIN1_SEG_VLD_FLAG'])
                    rm_buffer['SEG_ENER'].append(rm_buffer['WIN1_SEG_ENER'])
                    rm_buffer['SEG_WEIGHTED_ENER_LOW'].append(rm_buffer['WIN1_SEG_WEIGHTED_ENER_LOW'])
                    rm_buffer['SEG_LENGTH'].append(rm_buffer['WIN1_SEG_LENGTH'])
                    rm_buffer['SEG_WEIGHTED_ENER_HIGHT'].append(rm_buffer['WIN1_SEG_WEIGHTED_ENER_HIGHT'])

                    start += 2048

            rm_buffer['cnt'] = cnt

            # free the memory
            del rm_buffer['WIN1_PIXEL_VALUE']
            del rm_buffer['WIN1_PIXEL_OVER_FLAG']
            del rm_buffer['WIN1_SEG_Y']
            del rm_buffer['WIN1_SEG_X']
            del rm_buffer['WIN1_SEG_BKG']
            del rm_buffer['WIN1_SEG_VLD_FLAG']
            del rm_buffer['WIN1_SEG_ENER']
            del rm_buffer['WIN1_SEG_WEIGHTED_ENER_LOW']
            del rm_buffer['WIN1_SEG_LENGTH']
            del rm_buffer['WIN1_SEG_WEIGHTED_ENER_HIGHT']

            # data sending
            with app.app_context():
                sio.emit("lvds", dumps(rm_buffer), namespace='/')

            print(dumps(rm_buffer))

            # endtime = time.time()
            # print("total time:", endtime - startime)

        sio.sleep(0.05)


def main():
    # ConnectBox(interbox.sockctrl)
    # threading.Timer(0.5, b.aocsStep, (sio,)).start()
    # threading.Timer(1.0, b.lvdsStep).start()
    # threading.Timer(2.0, b.esimStep).start()
    # b = box('192.192.168.0.100')
    # threading.Timer(0.5, SendServerStat).start()
    port = 5000
    # get_lvds()
    threading.Timer(0.5, get_lvds).start()
    sio.run(app, host = '0.0.0.0', debug = False, port = port)


if __name__ == '__main__':
    main()

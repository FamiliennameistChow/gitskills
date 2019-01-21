from sys import argv
import eventlet
from eventlet.green import threading
from eventlet.green import socket
from eventlet import sleep
from struct import unpack, pack
from json import dumps, loads
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

import box
from decode_lvds2 import decode_data, decode_data, rmStruct, rmTree


try:
    boxA = argv[argv.index('-b') + 1]
except ValueError:
    boxA = '192.168.8.130'
except IndexError:
    boxA = '192.168.8.130'
finally:
    print("Box IP Address:", boxA)

try:
    port = int(argv[argv.index('-P') + 1])
except ValueError:
    port = 5000
except IndexError:
    port = 5000
finally:
    print("Web Port:", port)


# **************** flask *************************
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

# ************************************************


def get_lvds():

    def recvHead(s):
        try:
            string = ace.sock.recv(16)  # package_head
        except socket.error:
            string = ""
        except socket.timeout:
            string = ""
        # print(string)
        # return unpack((len(string) / 2) * 'H', string)
        # byte_s = "".join(string)
        # data = bytes.fromhex(byte_s)
        return string

    def recv(s, length):
        try:
            string = ace.sock.recv(length)
        except socket.error:
            string = ""
        except socket.timeout:
            string = ""
        # return unpack('>' + (len(string) / 2) * 'H', string)
        # byte_s = "".join(string)
        # data = bytes.fromhex(byte_s)
        return string

    # TCP connect
    ace = box.sock(boxA, 8990)
    ace.sock.settimeout(0.01)

    count_total = 0
    package = {}
    cnt = 0  # html view flag

    while True:
        head_info = recvHead(ace)

        if not head_info:
            continue

        lvds_head = unpack("<I", head_info[0:4])
        print(hex(lvds_head[0]))
        if hex(lvds_head[0]) == "0x5555aaaa":
            print("package head RIGHT")
        else:
            print("package head ERROR")
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

        package[package_count] = recv(ace, current_package_length)

        count = len(package[package_count])
        while count < current_package_length:
            package[package_count] += recv(ace, current_package_length - count)
            count = len(package[package_count])

        count_total += len(package[package_count])

        # joint the package
        if count_total == lvds_length:
            count_total = 0
            cnt += 1
            data = b''
            for i in range(package_total):
                data += package[i]

                # data processing
                rm_buffer = {}
                # startime = time.time()

                frame_head_scp = unpack('>H', data[0:2])[0]
                if hex(frame_head_scp) == '0x8a5c':
                    decode_data(rm_buffer, "CAK_TST_SCP", data[0:2048])
                    data_CAK_TST_THR = data[2048: 4096]
                    decode_data(rm_buffer, "CAK_TST_THR", data_CAK_TST_THR[0:2048])
                data = data[4096:]
                start = 0
                end = 0
                ncnt = 0
                
                while start != '0x8a' or end != '0x5b':
                    start = hex(data[ncnt])
                    end = hex(data[ncnt + 1])
                    ncnt += 2
                decode_data(rm_buffer, "SUBWIN_DAT", data[ncnt - 2:])

                rm_buffer['cnt'] = cnt

                # 数据发送
                sio.emit("lvds", dumps(rm_buffer), namespace='/')
                print(rm_buffer)

        sleep(0.05)


def main():
    # port = 5000
    # get_lvds()
    threading.Timer(0.5, get_lvds).start()
    sio.run(app, host = '0.0.0.0', debug = False, port = port)


if __name__ == '__main__':
    main()


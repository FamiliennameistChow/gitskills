from sys import argv
from eventlet.green import socket
from eventlet import sleep
from struct import unpack, pack
import box

try:
    boxA = argv[argv.index('-b') + 1]
except ValueError:
    boxA = '192.168.0.25'
except IndexError:
    boxA = '192.168.0.25'
finally:
    print("Box IP Address:", boxA)


def get_lvds():
    def recvHead(s):
        try:
            string = ace.sock.recv(16)  # package_head
        except socket.error:
            string = ""
        except socket.timeout:
            string = ""
        # return unpack((len(string) / 2) * 'H', string)
        byte_s = "".join(string)
        data = bytes.fromhex(byte_s)
        return data

    def recv(s, length):
        try:
            string = ace.sock.recv(length)
        except socket.error:
            string = ""
        except socket.timeout:
            string = ""
        # return unpack('>' + (len(string) / 2) * 'H', string)
        byte_s = "".join(string)
        data = bytes.fromhex(byte_s)
        return data

    ace = box.sock(boxA, 10003)
    ace.sock.settimeout(0.01)

    head_info = recvHead(ace)
    print(head_info)

    package = recv(ace, 1024)
    print(package)

    sleep(0.05)


get_lvds()





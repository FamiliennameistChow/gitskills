import socket
import os

BUFSIZE = 4096
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dir = os.path.join(os.getcwd(), "package")
print(dir)

client.connect(('192.168.0.90', 8990))

while True:
    for i in range(10):
        filename = 'package'+"_" + str(i) + ".txt"
        with open(os.path.join(dir, filename), 'r') as f:
            arr = []
            for line in f:
                arr += line.split()
                # print(arr)
            res = [x for x in arr]
            s = "".join(res)
            data = bytes.fromhex(s)
            # print(data)
        # ip_port = ('192.168.8.130', 8990)
        client.send(data)
        # client.send(data[16:])


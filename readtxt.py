# conding=utf-8
import os

i = 0
list = ["孔型: A", "孔型: B", "孔型: C", "孔型: D", "孔型: E", "孔型: F", "孔型: G", "孔型: H", "孔型: I", "孔型: J", "孔型: k"]
dataroot = "./data_all.txt"
with open(dataroot) as f:
    # lines = f.readline().decode('utf-8')
    for line in f.readlines():
        line = line[:-1]
        if line.find(list[i]) == -1:
            data = [line.split(' ')[1], line.split(' ')[4]]
            inputdata = (str(data[0]) + " " + str(data[1]))
            fp.writelines(inputdata + '\n')
            print(data)
        else:
            i += 1
            fp = open(os.path.join("./" + str(list[i - 1].split(' ')[-1]) + ".txt"), 'w')
            if i >= len(list):
                i = len(list) - 1
        print(list[i-1])

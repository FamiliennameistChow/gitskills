import os

dataroot = "./data.txt"

with open(dataroot) as f:
    for line in f.readlines():
        if line == "孔型A"：
            line += 1    
            line = line.split(' ')[1]
            print(line)

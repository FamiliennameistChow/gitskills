import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.font_manager import FontProperties
import csv

'''读取csv文件'''


def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


def readcsv(files):
    csvfile = open(files, 'r')
    plots = csv.reader(csvfile, delimiter=',')
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    row_num = 0
    for row in plots:
        if row_num == 0:
            row_num += 1
            continue
        x1.append((row[0]))
        x2.append((row[1]))
        x3.append((row[2]))
        x4.append((row[3]))
    return x1, x2, x3, x4


mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

plt.figure()
time, step, value_gray, value = readcsv("data1_gray.csv")
time = [float(x) for x in time]
step = [int(x)for x in step]
value_gray = [float(x) for x in value_gray]
value = [float(x)for x in value]

value_av = moving_average(interval = value, window_size = 3)  # 数据平滑处理

plt.plot(step, value_gray, color='red', label='value_gray', linewidth=1.0)
plt.plot(step, value, color='green', label='value', linewidth=1.0)
plt.plot(step, value_av, color='yellow', label='value', linewidth=1.0)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.ylim(0, 0.6)
plt.xlim(0, 200)
plt.xlabel('Steps', fontsize=10)
plt.ylabel('loss', fontsize=10)
plt.legend(fontsize=10)
plt.show()

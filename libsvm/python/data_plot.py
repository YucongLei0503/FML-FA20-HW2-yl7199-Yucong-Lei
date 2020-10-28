from __future__ import print_function
from array import array
import sys

import matplotlib.pyplot as plt



__all__ = ['plot_data','plot_ten_fold','plot_sv']

def plot_data(data_file_name, return_scipy=False):
    para = []
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    for i, line in enumerate(open(data_file_name)):
        line = line.split(",")
        para.append(float(line[0]))
        res1.append(1.0-float(line[1]))
        res2.append(1.0-float(line[2]))
        res3.append(1.0-float(line[3]))
        res4.append(1.0-float(line[4]))
    plt.plot(para, res1, label = "d = 1")
    plt.plot(para, res2, label = "d = 2")
    plt.plot(para, res3, label = "d = 3")
    plt.plot(para, res4, label = "d = 4")
    plt.xlabel('C')
    plt.ylabel('Cross Validation Error')
    plt.legend()
    plt.show()
    return

def plot_ten_fold(data_file_name, return_scipy=False):
    para = []
    res = []
    for i, line in enumerate(open(data_file_name)):
        line = line.split(",")
        para.append(int(line[0]))
        res.append(1.0-float(line[1]))
    plt.plot(para, res)
    plt.xlabel('d')
    plt.ylabel('Cross Validation Error of Ten Fold')
    plt.legend()
    plt.show()
    return

def plot_sv(data_file_name, return_scipy=False):
    para = []
    res1 = []
    res2 = []
    for i, line in enumerate(open(data_file_name)):
        line = line.split(",")
        para.append(float(line[0]))
        avg1 = 0
        avg2 = 0
        for k in range(10):
            avg1 = avg1 + int(line[k+2])
            avg2 = avg2 + int(line[k+12])
        res1.append(int(avg1 / 10))
        res2.append(int(avg2 / 10))
    plt.plot(para, res1, label = "average nSV")
    plt.plot(para, res2, label = "average nBSV")
    plt.xlabel('d')
    plt.ylabel('number of SV')
    plt.legend()
    plt.show()
    return
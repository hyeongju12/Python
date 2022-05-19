# note2 함수로 변경 > 절차지향 프로그래밍
from cmath import sqrt
from openpyxl import *
import math

import openpyxl

def get_data(filename):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    dic = {}
    for name, score in g:
        dic[name.value] = score.value

    return dic

def average(scores):
    s = 0
    for score in scores:
        s += score
    
    avrg = s / len(scores)
    avrg = round(avrg, 1)
    return avrg

def variance(scores, avrg):
    s = 0
    for score in scores:
        s += (score- avrg) ** 2
    
    variance = round(s/len(scores), 1)
    return variance

def std_dev(variance):
    std_dev = round(math.sqrt(variance), 1)
    return std_dev

def evaluation(average, total_avrg, std_dev, std_normal):
    if average < total_avrg and std_dev < std_normal:
        print("처참")

    elif average > total_avrg and std_dev < std_normal:
        print("전체적으로  골고루 잘함")

    elif average < total_avrg and std_dev > std_normal:
        print("일부만 잘함")

    elif average > total_avrg and std_dev > std_normal:
        print("전체적으로 잘하는거 같지만 일부만 잘함")

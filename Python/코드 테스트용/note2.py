'''
    절차지향 프로그래밍(Procedural Programming)
    함수(프로시저)를 사용해 프로그래밍하는 것

'''
from sys import stderr
from openpyxl import * 
import math
wb = load_workbook('C:/Users/Ayaan/Desktop/vscode_workspace/python_study/Python/class_2_3.xlsx')
wb.worksheets

ws = wb.active
ws

g = ws.rows

raw_data = {}
for name, score in g:
    raw_data[name.value] = score.value

scores = list(raw_data.values())

s = 0
for score in scores:
    s += score
avrg = round(s/len(scores), 1)

s = 0

for score in scores:
    s += (score-avrg) ** 2

variance = round(s/len(scores), 1)

std_dev = round(math.sqrt(variance))

print("평균 : {}, 분산 : {}, 표준편자 : {}".format(avrg, variance, std_dev))

if avrg < 50 and std_dev > 20:
    print("성적이 저조하고 학생간 실력 차이가 큽니다.")
elif avrg > 50 and std_dev > 20:
    print("성적은 평균 이상이지만 학생간 실력 차이가 큽니다.")
elif avrg > 50 and std_dev < 20:
    print("성적도 좋고 학생 간 실력 차이가 크지 않습니다.")
elif avrg < 50 and std_dev < 20:
    print("성적도 낮고 학생간 실력 차이가 큽니다.")
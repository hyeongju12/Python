# 소수소수
from tkinter import N


counter = 0

n = int(input("구간을 입력하세요 : "))

for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        counter+=1
        print(i)

print(f"카운트 수 : {counter}")

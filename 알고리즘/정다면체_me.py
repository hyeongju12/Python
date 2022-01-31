'''
문제 설명
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하세요.(정답이 여러 개일 경우 오름차순으로 출력)

입력 설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중 하나입니다.

출력 설명
첫 번째 줄에 답을 출력합니다. 
'''

import sys

from numpy import integer
sys.stdin = open('input2.txt', 'r')

num1, num2 = map(int, input().split())
print(num1, num2)

cnt = [0 for i in range((num1+num2))]

max_num = 0
sum_val = 0
res = []

for i in range(1, num1+1):
    for j in range(1, num2+1):
        sum_val = i + j
        cnt[sum_val-1] += 1

for idx, x in enumerate(cnt):
    if max_num < x:
        max_num = x

for idx, x in enumerate(cnt):
    if x == max_num:
        print(idx+1, end=' ')
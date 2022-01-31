'''
문제설명
N개의 자연수가 입력되면 각 자연수의 자릿수 합을 구하고, 그 합이 최대인 자연수를 출력하는
프로그램을 작성하세요.(각 자연수의ㅏ 자릿수의 합을 구하는 함수 : def digit_sum(x))

입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인
숫자를 출력한다.
'''

import sys
sys.stdin = open('input3.txt', 'r')
n = int(input())
m = list(map(int, input().split()))

split_res = []
sum_val = []
max_val = 0
max_idx = 0

for i in range(len(m)):
    split_res.append(list(map(int, str(m[i]))))
    sum_val.append(sum(split_res[i]))

    if max_val < sum_val[i]:
        max_val = sum_val[i]
        max_idx = i

print(m[max_idx])
# for i in range(len(m)):


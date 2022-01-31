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
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

max=float('-inf')

for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)

'''
def digit_sum(x):
    sum = 0
    for i in  str(x):
        sum += int(i)
   return sum 
'''
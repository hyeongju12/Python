'''
문제 설명
1에서 6까지의 눈을 가진 3개의 주사위를 던져 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10000원 + (같은 눈) * 1000원의 상금을 받는다.
규칙(2) 같은 눈이 2개가 나오면 1000원 + (같은 눈) * 100원의 상금을 받는다.
규칙(3) 모두 다른 눈이 나오는 경우 (그 중 가장 큰 눈) * 100원의 상금을 받는다.

입력 설명
첫째 줄에는 참여하는 사람 수 N이 주어지고 그 다음 줄 부터 N개의 줄에 사람들이 주사위를
던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력 설명
첫쨰 줄에 가장 많은 상금을 받은 사람의 상금 출력
'''

import sys

sys.stdin = open('input5.txt', 'rt')
n=int(input())
res=0

for i in range(n):
    tmp=input().split()
    print(tmp)
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c:
        money = 10000 + a*1000
    elif a==b or a==c:
        money = 1000 + a*100 
    elif b==c:
        money = 1000 + b*100
    else:
        money = c*100
    if money > res:
        res=money
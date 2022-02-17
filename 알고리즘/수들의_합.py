'''
문제설명
N개의 수로 된 수열 A[1], A[2], ~~~. A[N]이 있다. 이 수열의 i번째 수부터 j번쨰 수까지 합
A[i] + A[i+1] ~~ A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성

입력설명
첫 줄에는 N과 M이 주어진다.
다음줄에는 A[1] ~ A[N]이 공백으로 분리되어 주어진다.

출력설명
경우의 수를 출력하시오
'''
import sys
sys.stdin = open('input11.txt', 'r')
n, m = map(int, input().split())
A = list(map(int, input().split()))
lt=0
rt=1
cnt=0
tot=A[0]

while True:
    if tot<m:
        if rt<n:
            tot+=A[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=A[lt]
        lt+=1
    else:
        tot-=A[lt]
        lt+=1

print(cnt)

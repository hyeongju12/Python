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
sys.stdin = open('input2.txt', 'r')
n, m = map(int, input().split())

cnt = [0 for i in range(n+m)]
max_val = float('-inf')

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j - 1] += 1

print(cnt)

for i in range(len(cnt)):
    if max_val < cnt[i]:
        max_val = cnt[i]

for i in range(len(cnt)):
    if max_val == cnt[i]:
        print(i+1, end=' ')
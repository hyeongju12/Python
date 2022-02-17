'''
문제설명
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력
하는 프로그램을 작성

입력설명
첫 줄에 첫 번째 리스트의 크기
두 번째줄에 N개의 리스트 원소가 오름차순으로 주어진다.
세 번째줄에 두 번쨰 리스트의 크기가 주어진다.
네 번쨰 줄에  M개의 리스트 원소가 오름차순으로 주어진다. 

출력설명
오름차순으로 정렬된 리스트 출력
'''
import sys
sys.stdin =open('input10.txt', 'r')

n = int(input())
n_list = list(map(int, input().split()))
print(n_list)

m = int(input())
m_list = list(map(int, input().split()))
print(m_list)

p1 = p2 = 0
c = []

while p1<n and p2<m:
    if n_list[p1] <= m_list[p2]:
        c.append(n_list[p1])
        p1+=1
    else:
        c.append(m_list[p2])
        p2+=1

if p1<n:
    c=c+n_list[p1:]
if p2<m:
    c=c+m_list[p2:]



for x in c:
    print(x, end=' ')
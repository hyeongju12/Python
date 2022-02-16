'''
문제설명
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 있다.(오름 차순 정렬), 각 카드는 1 부터 20까지 나타낸다.
구간 [a, b]가 주어지면 a부터 b까지 카드를 현재의 역순으로 놓는다.
이 상태에서 구간 [9,13]이 다시 주어진다면, 다시 역순으로 놓는다. 

입력설명
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번쨰 줄에는 i번쨰 구간의 시작 위치
ai와 끝위치 bi가 차례로 주어진다.(범위는 1<= ai <= bi < 20)

출력설명
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집는
작업을 했을떄 마지막 카드들의 배치를 한 줄에 출력하라
'''
import sys
sys.stdin = open('input9.txt', 'r')

card = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end-start+1)//2):
        card[start+i], card[end-i] = card[end-i], card[start+i]
card.pop(0)

print(card)

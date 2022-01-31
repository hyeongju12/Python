'''
문제 설명
N명의 학생의 점수가 주어지고, 평균과 가장 가까운 점수를 출력하는데, 동일한 점수가 있을 경우
번호가 빠른 학생 번호를 답으로 하고, 점수의 차가 동일할 떄 큰 점수를 가진 학생의 번호를 답으로 한다.

입력 설명
첫줄에 자연수가 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 삭생의 수학점수인 N개의 자연수가 주어진다.

출력 설명
첫줄에는 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫쨰 자리에서 반올림 힌다.
'''

import sys
sys.stdin = open('input1.txt', 'r')

a = list(map(int, input().split()))
print(a)

ave = round((sum(a)/len(a))+0.5)
cmp = float('inf')

for idx, x in enumerate(a):
    print('학생번호 : {0}, 점수 : {1}'.format(idx+1, x))
    tmp = abs(a[idx]-ave)

    if cmp > tmp:
        cmp = tmp
        score = x
        student_num = idx+1
    elif cmp == tmp:
        if x > score:
            student_num = idx+1

print(ave, student_num)

'''
에라스토테네스의 체(소수를 찾는 방법)
1. 2부터 소수를 구하고자 하는 수를 나열
2. 2를 제외한 2의 배수를 모두 지운다.
3. 3을 제외하고 3의 배수를 모두 지운다.
4. 5를 제외하고 5의 배수를 모두 지운다.
5. 7을 제외하고 7의 배수를 모두 지운다. 
6. 위 구간을 반복하면 해당 구간의 소수가 남는다.

문제 : 구간 내 소수의 갯수를 구하시오.
'''

import sys

sys.stdin = open('input4.txt', 'r')

n = int(input())
ch = [0]*(n+1)
cnt = 0
list_val = []

for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        list_val.append(i)
        # ch[2]==0 -> cnt = 1
        for j in range(i, n+1, i):
            # 2의 배수인 인덱스를 가지는 리스트의 값을 1로 변경
            # 2의 배수는 cnt에서 카운트 되지 않음
            ch[j]=1

print(cnt)
print(list_val)
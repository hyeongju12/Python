import sys
from unittest import result
sys.stdin=open('input1.txt', 'r')
# n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/len(a))
print(a)
print(ave)

result = 0
tmp = 0
tmp_list = []

for i in range(len(a)):
    tmp = abs(a[i] - ave)
    tmp_list.append(tmp)

arrMin = float('inf')
for j in range(len(tmp_list)):
    if arrMin > tmp_list[j]:
        arrMin = tmp_list[j]
        result = a[j]
        

print('평균에서 제일 가까운 값은 : {}'.format(result))
    
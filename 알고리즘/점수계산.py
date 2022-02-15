import sys
sys.stdin = open('input6.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for i in a:
    if i == 1:
        cnt += 1
        sum += cnt

    elif i == 0:
        cnt = 0

print(sum)

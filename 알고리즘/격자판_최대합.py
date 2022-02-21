import sys
sys.stdin = open('input12.txt', 'r')

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

max = 0
row_sum = 0
col_sum = 0
dia_sum = 0
r_dia_sum = 0
x = y = 0

for i in range(n):
    for j in range(n):
            row_sum = 0
            col_sum = 0
            row_sum += a[i][j]
            col_sum += a[j][i]
            if max < row_sum:
                max = row_sum
            if max < col_sum:
                max = col_sum


for i in range(n):
    r_dia_sum += a[i][i]
    dia_sum += a[i][n-i-1]
    if max < r_dia_sum:
        max = r_dia_sum
    if max < dia_sum:
        max = dia_sum
        
print(max)
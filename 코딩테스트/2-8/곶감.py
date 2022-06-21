import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
items =[list(map(int, input().split())) for _  in range(n)]
round = int(input())
for i in range(round):
	lt, rt, k = map(int, input().split())
	if rt == 0:
		for _ in range(k):
			items[lt - 1].append(items[lt - 1].pop(0))
	else:
		for _ in range(k):
			items[lt - 1].insert(0, items[lt-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
	for j in range(s, e+1):
		res+=items[i][j]
	if i<n//2:
		s += 1
		e -= 1
	else:
		s -= 1
		e += 1

print(res)
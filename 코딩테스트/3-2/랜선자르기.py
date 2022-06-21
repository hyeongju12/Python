import sys
sys.stdin = open('input.txt', 'r')

def Count(len):
	cnt = 0
	for x in Line:
		cnt+=(x//len)
	return cnt

n, m = map(int, input().split())
Line = []
res = 0
largest = 0

for i in range(n):
	tmp = int(input())
	Line.append(tmp)
	largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
	mid = (lt+rt) // 2
	if Count(mid) >= m:
		res = mid
		lt = mid+1
	else:
		rt = mid-1

print(res)




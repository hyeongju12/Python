from typing import MutableSequence


def bubble_sort(x: MutableSequence) -> None:
	n = len(x)

	ccnt = 0 #비교횟수
	scnt = 0 #교환횟수

	for i in range(n-1):
		print(f'{i+1}번째 패스')
		for j in range(n-1, i, -1):
			for m in range(0, n-1):
				print(f'{x[m]: 2}' + ('  ' if m != j -1 else ' +' if x[j-1] > x[j] else ' - '), end=' ')
			ccnt += 1
			if x[j-1] > x[j]:
				scnt += 1
				x[j-1], x[j] = x[j], x[j-1]
		for m in range(0, n-1):
			print(f'{x[m]:2}', end='  ')
		print(f'{x[n-1]:2}')
	print(f'비교를 {ccnt}번 했습니다.')
	print(f'비교를 {scnt}번 했습니다.')


if __name__ == "__main__":
	print("버블 정렬 복습")

	num = int(input("배열의 갯수 입력 :"))
	x = [None] * num

	for i in range(len(x)):
		x[i] = int(input(f'x[{i}] : '))

	bubble_sort(x)

	for i in range(len(x)):
		print(f'x[{i}] = {x[i]}')
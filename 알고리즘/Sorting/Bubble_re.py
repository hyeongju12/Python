from typing import MutableSequence


def bubble_sort(x : MutableSequence) -> None:
	n = len(x)

	left = 0
	right = n - 1
	last = right

	while left < right:
		for j in range(right, left, -1):
			if x[j-1] > x[j]:
				x[j-1], x[j] = x[j], x[j-1]
				last = j
		left = last

		for j in range(left, right):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
				last = j
		right = last

if __name__ == "__main__":
	print('버블정렬을 실행합니다.')
	num = int(input('원소 수를 입력하세요'))
	x = [None] * num

	for i in range(num):
		x[i] = int(input(f'x[{i}]  : '))

	bubble_sort(x)

	print("오름차순으로 정리했습니다.")
	for i in range(num):
		print(f'x[{i}] = {x[i]}')
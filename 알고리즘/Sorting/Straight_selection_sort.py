from typing import MutableSequence


def straight_select_sort(x : MutableSequence):
	n = len(x)
	for i in range(n-1):
		min = i
		for j in range(i+1, n):
			if x[j] < x[min]:
				min = j
		x[i], x[min] = x[min], x[i]


if  __name__ == "__main__":
	print("단순 선택 정렬")

	num = int(input("원소의 갯수를 입력해주세요 : "))
	x = [None] * num

	for i in range(len(x)):
		x[i] = int(input(f'x[{i}] : '))

	straight_select_sort(x)

	for i in range(len(x)):
		print(f'x[{i}] : {x[i]}')


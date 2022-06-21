from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
	n = len(a)

	for i in range(n-1):
		for j in range(n-1, i, -1):
			if a[j-1] > a[j]:
				a[j-1], a[j] = a[j], a[j-1]


if __name__ == "__main__":
	print("버블 정렬 복습")

	num = int(input("배열의 갯수 입력 :"))
	x = [None] * num

	for i in range(len(x)):
		x[i] = int(input(f'x[{i}] : '))

	bubble_sort(x)

	for i in range(len(x)):
		print(f'x[{i}] = {x[i]}')

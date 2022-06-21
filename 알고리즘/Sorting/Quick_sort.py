from typing import MutableSequence


def qsort(a: MutableSequence, left, right) -> None:
	n = len(a)

	pl = left
	pr = right
	x = a[left+right//2]

	while pl <= pr:
		while a[pl] <= x : pl += 1
		while a[pr] >= x : pr -= 1
		if pl <= pr:
			a[pl], a[pr] = a[pr], a[pl]
			pl += 1
			pr -= 1

	if left < pr : qsort(a, left, pr)
	if pl < right : qsort(a, pl, right)


def quick_sort(a: MutableSequence):
	qsort(a, 0, len(a) - 1)


if __name__ == "__main__":
	print("배열을 나눕니다.")
	num = int(input("배열의 크기 입력해주세요 : "))
	x = [None] * num

	for i in range(num):
		x[i] = int(input(f'x[{i}] : '))

	quick_sort(x)
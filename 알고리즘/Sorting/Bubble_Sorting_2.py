from typing import MutableSequence

def bubble_sort(x: MutableSequence) -> None:
	n = len(x)

	for i in range(n-1):
		for j in range(n-1, i, -1):
			ccnt = 0
			if x[j-1] > x[j]:
				x[j-1], x[j] = x[j], x[j-1]
				ccnt += 1
			if ccnt == 0:
				break

if __name__ == '__main__':

	print("개선된 버블 정렬")
	print("교환 횟수가 없을 경우 종료됩니다.")

	num = int(input(f'배열의 길이를 입력하세요 :'))
	x = [None] * num

	for i in range(len(x)):
		x[i] = int(input(f'x[{i}] : '))

	bubble_sort(x)



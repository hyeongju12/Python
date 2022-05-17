def quick_sort(data, start, end):
	if start >= end:
		return

	left = start
	right = end
	pivot = data[(start+end)//2]

	def quick_sort(data, start, end):
		while left <= start:
			while data[left] < pivot:
				while data[right] > pivot:
					right -= 1

				if left <= right:
					data[left], data[right] = data[right], data[left]
					left += 1
					right -= 1

	quick_sort(data, start, end)
	quick_sort(data, left, right)

if __name__ == "__main__":
	li = [2, 5, 4, 1, 8, 10, 5, 3, 6, 6, 5, 7, 9, 12, 11]
	quick_sort(li, 0, len(li)-1)
	print(li)
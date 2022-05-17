# def linear_search(data, target):
# 	for idx in range(len(data)):
# 		if data[idx] == target:
# 			return idx
# 	return None

def binary_search(data, target):
	data.sort()

	start = 0
	end = len(data) -1

	while start <= end:
		mid = (start + end) // 2

		if data[mid] == target:
			return mid

		elif data[mid] > target:
			end = mid - 1

		else:
			start = mid + 1

	return None


if __name__ == "__main__":
	data = [i**2 for i in range(1, 11)]
	target  = 9

	result = binary_search(data, target)
	print(result)
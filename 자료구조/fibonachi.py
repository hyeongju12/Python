def fibonacci(n):
	if n == 1:
		return 0

	if n == 2:
		return 1

	return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
	print(fibonacci(3))
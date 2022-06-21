#소수 판단하기

def prime_number(n):
	for x in range(2, n):
		for y in range(2, x):
			if x % y == 0:
				return f'{n}은 소수가 아닙니다.'
			return f'{n}은 소수입니다.'


if __name__ == "__main__":
	num = int(input())
	print(prime_number(num))
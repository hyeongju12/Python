while True:
    n = int(input('n 값을 입력하세요.'))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n+1):
    sum += i

print(f'1부터 n까지의 합은 {sum}입니다.')
# print("n자리수 까지 합 구하기.")

# n = int(input("n을 입력해주세요 :"))

print("a, b까지 합을 구하세용!")
a = int(input('a 값을 입력하세요 :'))
b = int(input('b 값을 입력하세요 :'))

if a > b:
    a, b = b, a

sum = 0

# while i <= n:
#     print(f'{i}값')
#     sum += i
#     i += 1

for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)

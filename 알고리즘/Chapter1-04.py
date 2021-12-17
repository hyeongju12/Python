print("+ 와 -를 줄바꿈 없이 번갈아 출력")

n = int(input("출력 개수 입력 :"))

# for i in range(1, n+1):
#     if i % 2:
#         print(f'+', end='')
#     else:
#         print(f'-', end='')

for _ in range(n//2):
    print("+-", end='')

if n % 2:
    print("+", end='')
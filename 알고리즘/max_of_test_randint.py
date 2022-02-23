from max import max_of
import random

print("난수의 최대값을 구합니다.")
num = int(input("난수의 개수를 입력하세요."))
lo = int(input("최소값을 입력"))
hi = int(input("최대값을 입력"))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{x}')
print(f'최대값은 : {max_of(x)}')
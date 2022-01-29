print('*를 출력합니다.')

n = int(input('몇 개를 출력할가요?'))
w = int(input('몇 개마다 줄바꿈 할까요?'))

# 방법1. 반복문에서 조건 판단하여 출력하기.
# for i in range(n):
#     print('*', end='')
#     if i % w == w-1:
#        print()

# 방법2. 반복문 사용하지 않고 출력하기
for _ in range(n // w):
    print('*' * w)

res = n % w
print('*' * res)
# x = ['John', 'George', 'Paul', 'Ringo']

# # 리스트의 모든 원소 스캔
# # for i in range(len(x)):
# #     print(f'[{i}] = {x[i]}')

# # enumerate로 스캔
# # for i, name in enumerate(x):
# #     print(f'[{i}] : {name}')

# # for i, name in enumerate(x, 1):
# #     print(f'[{i}] : {name}')

# y = [1,4,5,7,13,4,9]
# n = len(y)

# for i in range(n//2):
#     y[i] = y[n-1-i]

# print(y)
# x = [1,2,3,4,5]
# y = list(reversed(x))

# print(y)

n = int(input('10진수 값을 입력하시구려 : '))
n_2 = []

while True:
    b = n % 2
    n = n // 2
    n_2.append(b)
    print(n_2)
    if n == 0:
        break

print(n_2)
def sum_1ton(x):
    sum = 0
    while x > 0:
        sum += x
        x -= 1
    return sum


x = int(input("X 까지의 합을 구하시오! :"))
print(f'{x}까지의 합은 : {sum_1ton(x)}')

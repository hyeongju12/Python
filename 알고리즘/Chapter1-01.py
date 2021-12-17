print("세 정수 중 최대값을 구하시오 :")
a = int(input("정수를 입력하세요:"))
b = int(input("정수를 입력하세요:"))
c = int(input("정수를 입력하세요:"))

maximum = a

if maximum < b: maximum = b
if maximum < c: maximum = c

print(f'최대값은 {maximum}입니다.')
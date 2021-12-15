'''
1.1. integer
python에서 정수는 int로 나타내며 immutable이다.
immutable : 값이 변하지 않는다.
mutable : 값이 변한다.
ex) 
    x --> 1, y --> 1 
    y += 3
    x --> 1, y --> 4
'''


# n.bit_length() : n을 나타내는데 필요한 바이트 수 확인 
n = 999
val = n.bit_length()
print(val)


# int(정수)
s = '11'
val = int(s)
print(val)

# 정수가 아닌 숫자로 이루어진 문자열을 입력하면 ValueError 발생
# s2 = '11.25'
# val2 = int(s2)
# print(val2)

# 밑(Base) 사용
# base가 2면 s를 구성하는 숫자는 0, 1이여야 한다.
val3 = int(s, 2)
print(val3)

# float(부동소수점)
# 부동소수점은 이준수 분수로 표현되기 떄문에 함부로 비교하거나 빼면 안된다.
# 2진법으로 표현하기 어려운 숫자.(0.1)

print(bool(0.2 * 3 == 0.6))
print(bool(1.2 - 0.2 == 1.0))
print(bool(1.2 - 0.1 == 1.1))
print(0.1 * 0.1 == 0.01)

# 정수와 부동소수점 관련 메서드

# divmod(x, y) x를 y로 나눌때 (몫, 나머지)를 반환한다.
result = divmod(45, 6)
print(result)

# round(x, n) x를 n<0 경우 n자리수 만큼 반올림 한 값 반환, n>0 n자리로 반올림한 값을 반환
result1 = round(100.12, -2)
result2 = round(100.12, 2)

print(result1)
print(result2)

# as_integer_ratio() 부동소수점을 분수로 표현
result3 = 0.1.as_integer_ratio()
print(result3)

# 2진수, 8진수, 16진수
print(bin(999))
print(oct(999))
print(hex(999))
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


# 10진법으로 변환 
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
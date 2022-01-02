# Chapter4-3
# 시퀀스형
# 컨테이너(Container) 자료형 : 서로다른 자료형을 담을수 있는 것[list, tuple, collections.deque]
# 플랫(Flat) 자료형 : 단일 자료형만 담을 수 있다.[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블
# key에 Value를 저장하는 구조
# 파이썬 dict 해쉬 테이블 예)
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Hash 값 확인 (고유하다.)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) 

# Dict Setdefault 예제(레퍼런스 권장사항) /
source = (('k1', 'val1'),
        ('k1', 'val2'),
        ('k2', 'val3'),
        ('k2', 'val4'),
        ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)
# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
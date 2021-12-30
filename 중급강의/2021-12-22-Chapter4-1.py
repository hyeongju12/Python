# Chapter4-1
# 시퀀스형
# 컨테이너(Container) 자료형 : 서로다른 자료형을 담을수 있는 것[list, tuple, collections.deque]
# 플랫(Flat) 자료형 : 단일 자료형만 담을 수 있다.[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급

# 지능형 리스트(list comphrehension)

chars = '+_)(*&^%$#@!'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comphrehending lists
code_list2= [ord(s) for s in chars]

print(code_list2)

# Comphrehending lists
code_list3 = [ord(s) for s in chars if ord(s) > 40]

print(code_list3)

# list+map, filter
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list4)


#chr() : 유니코드를 문자로 변환, ord() : 문자를 유니코드로 변환

#Generator  생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
# [] 을 ()으로 바꾸면 제너레이터 생성
tuple_g = (ord(s) for s in chars)
array_g = array.array('I',(ord(s) for s in chars))

print(tuple_g)
print(array_g)
print(next(tuple_g))
# Chapter4-1
# 시퀀스형
# 컨테이너(Container) 자료형 : 서로다른 자료형을 담을수 있는 것[list, tuple, collections.deque]
# 플랫(Flat) 자료형 : 단일 자료형만 담을 수 있다.[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변), Immutable(불변)
l = (15, 20, 25)
s = [15, 20, 25]

print(l, id(l))
print(s, id(s))

l = l * 2
s = s * 2

print(l, id(l))
print(s, id(s))

l *= 2
s *= 2

print(l, id(l))
print(s, id(s))

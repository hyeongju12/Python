# Chapter6-1 병행성
# 병행성, 흐름제어
# 이터레이터
# 제너레이터
# __iter__, __next__
# 클래스 기반 제너레이터 구현

# 파이썬 제너레이터는 이터레이터를 리턴
# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args ~> iterable

# 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTU'

for c in t:
    print('>', c)

# while
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

# 반복형 확인
print(hasattr(t, '__iter__'))

from collections import abc
import collections

# print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))
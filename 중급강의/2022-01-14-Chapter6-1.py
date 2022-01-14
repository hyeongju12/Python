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

print()
print()

# __next__()
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양이 엄청 증가한 경우 메모리 사용량 증가 -> 이러한 상황을 피하고자 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine)구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제너레이터 / 리턴이 없어도됨..
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# Chapter6-3
# 병행성(Cocurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 => 속도
# 코루틴(Coroutine) : 

# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 스레드
# yield : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(수행제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 스레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착상태 발생 가능, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await


# 코루틴 EX1

def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# 제너레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
#next(cr1)

# send를 이용해서 메인 루틴과 서브 루틴이 데이터를 교환 할 수 있다. 
# 값이 없으면 None을 전달함.
# cr1.send(100)

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행상태
# GEN_SUSPEND : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(x))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate
from tkinter import Y

print(getgeneratorstate(cr3))

print(next(cr3))

cr3.send(100)

# 코루틴 EX3
# StopIteration  자동처리(3.5 -> await)
# 중첩 코루틴 정리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()

print(list(t2))

def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()

print(next(t3))
print(next(t3))

# Chater5-4
# 데코레이터
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결화, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용하기 용이하다.

# 단점
# 1. 가독성 저하
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습

import time

def perf_clock(func):
    def perf_clocked(*args):
        st = time.perf_counter()
        result = func(*args)
        et = time.perf_counter() - st
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)
@perf_clock
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, "Called None Decorator -> time_func")
print()
none_deco1(1.5)
print('-' * 40, "Called None Decorator -> sum_func")
print()
none_deco2(100, 200, 300, 400, 500)

time_func(1.5)
sum_func(100, 200, 300, 400, 500)
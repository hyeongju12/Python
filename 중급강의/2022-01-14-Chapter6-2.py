# Chapter6-2
# 병행성(Cocurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 => 속도

def generator_ex1():
    print('start')
    yield 'A point'
    print('Continue')
    yield 'B point'
    print('End')


temp = iter(generator_ex1())
# print(temp)

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp3:
    print(i)


print()
print()

# Generator Ex3(중요 함수)
# filterfalse, accumulate, chain, product, groupby

import itertools
gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
# 무한생성

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    pass
    # print(v)

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n <3 , [1,2,3,4,5])

for v in gen3:
    pass
    # print(v)

print()

# 누적합계
gen4 = itertools.accumulate([x for x in range(1,101)])

for v in gen4:
    pass
    # print(v)

# 연결1 : 두개의 이터러블한 객체가 있으면 연결할 수 있다.
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

# 연결2 ; 쌍으로 연결
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

#개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

#개별2
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

#그룹화
gen9 = itertools.groupby('AAABBBCCCDDDEEE')

for chr, group in gen9:
    print(chr, ' : ', list(group))

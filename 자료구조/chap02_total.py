'''
자료구조와 배열

배열의 장점 
- 변수를 하나로 묶어서 사용할 수 있어 코드를 쉽고 효율적으로 작성가능
- 서로 다른 자료형을 사용 할 수 있음

파이썬에서의 배열
- 파이썬에서는 배열을 리스트와 튜플로 구현 가능하다
  * 리스트 : mutable, 튜플 : immutable
'''

# 리스트
list0 = []
list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
list3 = list()
list4 = list('ABC') # 'A', 'B', 'C' 문자열 리스트 생성
list6 = list([1,2,3]) # 리스트 원소로 부터 리스트 생성
list7 = list((1,2,3)) # 튜플 원소로 부터 리스트 생성
list8 = list({1,2,3}) # 집합으로 부터 리스트 생성

#print(list4)
#print(list6)
#print(type(list7))
#print(type(list8))

# 특정 범위의 정수를 가지는 리스트 생성 => range함수와 조합하여 생성
list9 = list(range(4, 10))
#print(list9)

# 원소값을 정하지 않은 리스트는 None을 사용해 만들 수 있다. 
list10 = [None] * 10
#print(list10)

# 튜플 * 원소가 한개여도 , 을 사용해야한다. 없으면 단순 변수로 인식하기 때문
tuple01 = ()
tuple02 = 1,
tuple03 = (1,)

print(tuple02)

tuple04 = tuple()
tuple05 = tuple('ABC')
tuple06 = tuple([1, 2, 3]) 
tuple07 = tuple({1, 2, 3})

print(tuple06)
print(tuple07)

tuple08 = tuple(range(7))
tuple09 = tuple(range(3, 8))
tuple10 = tuple(range(3, 13, 2))

print(tuple08)
print(tuple09)
print(tuple10)

# 우변의 원소를 좌변의 변수에 한번에 대입, 이와 같이 리스트나 튜플의 
# 원소값을 풀어 여러 변수에 대입하는 것을 Unpack이라고 한다. 
x = [1,2,3]
a, b, c = x


# 리스트 인덱스 접근
x = [11,22,33,44,55,66,77,88,99]

print(x[1])
print(x[-1])
print(x[-2])

# 리스트 슬라이스 접근
print(x[0:len(x)+1])
print(x[0:10:2])
print(x[-1:-10:-1])
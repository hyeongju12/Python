# globar variable(전역변수)

'''
함수 안에서 전역변수 값을 변경하려면  global으로 선언해야 
전역변수에 값을 바꿀 수 있다.
'''

'''
g_var = 10

def func():
    global g_var
    g_var=20
    print('전역변수 : {}'.format(g_var))


if __name__ == "__main__":
    func()
    print(g_var)

'''


# Local variable(지역변수)
# inner 함수에서 outer함수의 변수의 값을 바꾸고자 할때 nonlocal 선언하면 된다. 

'''
a = 1

def outer():
    b = 2
    c = 3
    print(a, b, c)
    def inner():
        nonlocal b, c
        b = 20
        c = 30
        d = 4
        e = 5
        print(a, b, c, d, e)
    inner()

if __name__ == "__main__":
    outer()
'''
def change_value(x, value):
    x = value
    print('x : {} in change_value'.format(x))

if __name__ == "__main__":
    x = 10
    change_value(x, 20)
    print("x : {} in main".format(x))

    # 파이썬에서는 객체 참조에 의한 전달(call by object reference) 사용한다.
    # 객체 참조에 의한 전달 방식의 메모리 관리는 가비지 컬렉션 기법을 사용하고
    # 파이썬에서는 레퍼런스 카운트 알고리즘을 사용한다. 
    # 10이라는 정수형 객체를 a, b 가 참조하고 있으면 referencecount 값은 2가 되고
    # a, b의 10에 대한 참조가 종료되면 reference count값이 0이되고 메모리상에서 객체가 삭제된다.
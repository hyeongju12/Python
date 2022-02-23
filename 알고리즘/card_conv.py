def card_conv(x:int, r:int) -> str:
    '''정수 x를 r 진수로 변환하고 그 수를 str형으로 리턴'''
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')
    while x>0:
        print('    +'+(n+2) * '-')
        if x // r:
            print(f'{r:2} | {x//r:{n}d} ---> {x % r}')
        else:
            print(f'      | {x//r:{n}d} ---> {x % r}')
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    while True:
        while True:
            no = int(input("음수가 아닌 정수를 입력하라 : "))
            if no > 0:
                break

        while True:
            cd = int(input('어떤 진수 ? :'))
            if 2 <= cd <= 36:
                break

        print(f'{cd} 진수로는 {card_conv(no, cd)} 입니다.')
        
        retry = input("한번 더 ? Y(y), N(n)")
        if retry in {'N', 'n'}:
            break



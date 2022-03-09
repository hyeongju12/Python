from enum import Enum
from typing import Any
import hashlib

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' :'))
        if 1 <= n <= len(Menu):
            return Menu(n)

class Node: # 해시를 구성하는 노드
    def __init__(self, key: Any, value: Any, next: None) -> None:
        self.key = key #키
        self.value = value # 값
        self.next = next # 다음 노드 참조

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시 테이블 크기 지정
        self.table = [None] * self.capacity # 해시 테이블 선언

    def hash_value(self, key: Any) -> int:
        # 해시값을 구하는 문장
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()

hash = ChainedHash(13)

while True:
    menu = select_menu()
    if menu == Menu.추가 :
        key = int(input('추가할 키를 입력하세요 : '))
        val = input('추가할 값을 입력하세요')
        if not hash.add(key, val):
            print('추가 실패!')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요 : '))
        if not hash.remove(key):
            print('삭제 실패!')

    elif menu == Menu.검색 :
        key = int(input('검색할 키를 입력하세요 : '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키가 갖는 값은 {t} 입니다.')
        else:
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.덤프:
        hash.dump()

    else:
        break



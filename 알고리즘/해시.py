from typing import Any
import hashlib

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
from typing import Any
from collections import deque

class Stack:
    def __init__(self, maxlen):
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self):
        return len(self.__stk)

    def is_empty(self):
        return not self.__stk

    def is_full(self):
        return len(self.__stk) == self.capacity

    def push(self, value):
        self.__stk.append(value)

    def pop(self):
        self.__stk.pop()

    def peek(self):
        return self.__stk[-1]

    def clear(self):
        return self.__stk.clear()

    def find(self, value):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value):
        return self.__stk.count(value)

    def __contains__(self, value):
        return self.count(value)


    def dump(self):
        print(list(self.__stk))

    

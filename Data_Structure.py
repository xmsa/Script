from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()
    def __str__(self):
        return str(self.__data)
    def enqueue(self, item):
        self.__data.append(item)
    def dequeue(self):
        return self.__data.popleft()
    def is_empty(self):
        return len(self.__data) == 0
    def __len__(self):
        return len(self.__data)
    def __getitem__(self, index):
        return self.__data[index]
    def __setitem__(self, index, value):
        self.__data[index] = value
    def __delitem__(self, index):
        del self.__data[index]

class Stack:
    def __init__(self):
        self.__data = deque()
    def __str__(self):
        return str(self.__data)
    def push(self, item):
        self.__data.append(item)
    def pop(self):
        return self.__data.pop()
    def is_empty(self):
        return len(self.__data) == 0
    def __len__(self):
        return len(self.__data)
    def __getitem__(self, index):
        return self.__data[index]
    def __setitem__(self, index, value):
        self.__data[index] = value
    def __delitem__(self, index):
        del self.__data[index]
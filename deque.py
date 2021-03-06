class Deque:
    def __init__(self):
        self.__deque = []
        self.__head = None
        self.__tail = None
    
    @property
    def deque(self):
        return self.__deque

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def push_right(self, value):
        if len(self.__deque) == 0:
            self.__deque.append(value)
            self.__tail = value
            self.__head = value
        else:
            self.__deque.append(value)
            self.__tail = value

    def push_left(self, value):
        if len(self.__deque) == 0:
            self.__deque.insert(0,value)
            self.__tail = value
            self.__head = value
        else:
            self.__deque.insert(0,value)
            self.__head = value
    
    def pop_left(self):
        if len(self.__deque) == 0:
            self.__tail = None
            self.__head = None
        elif len(self.__deque) == 1:
            self.__deque.pop(0)
            self.__tail = None
            self.__head = None
        else:
            self.__deque.pop(0)
            self.__head = self.__deque[0]

    def pop_right(self):
        if len(self.__deque) == 0:
            pass
        elif len(self.__deque) == 1:
            self.__deque.pop()
            self.__tail = None
            self.__head = None
        else:
            self.__deque.pop()
            self.__tail = self.__deque[-1]


if __name__ == '__main__':
    d1=Deque()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_left(10)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_left(-10)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_left(-20)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_left(-30)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_right(20)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_right(30)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)
    d1.push_right(40)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    print('-------------------------')

    d1.pop_left()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.pop_right()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

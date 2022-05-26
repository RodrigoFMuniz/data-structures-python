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
            self.__tail = value
            self.__head = value
        else:
            self.__tail = value
        
        self.__deque.append(value)


    def push_left(self, value):
        self.__deque.insert(0,value)
        self.__head = value


if __name__ == '__main__':
    d1=Deque()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

    d1.push_right(10)
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

    d1.push_right(20)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('deque:',d1.deque)

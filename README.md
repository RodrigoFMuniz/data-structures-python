# Data Structures

## What is data structure?

    Disciplina que estuda as técnicas computacionais
    para a organização e manipulação eficiente de
    quaisquer quantidades de informações

## Using It to solve problems

## Problem example

1.  Temos uma rede de dispositivos eletrônicos. Tais dispositivos
    estão interligados por canais de comunicação. Cada canal tem
    um valor associado C (número real no intervalo 0 ≤ C ≤ 1) que
    representa sua confiabilidade. Interpreta-se como
    confiabilidade a probabilidade de que o canal não venha a
    falhar. Forneça um algoritmo para encontrar o caminho mais
    confiável entre dois dispositivos dados

### Stack

    class Stack:
        def __init__(self):
            self.stack = []

        def push(self,item):
            self.stack.append(item)

        def pop(self):
            if self.length() == 0:
                return None
            else:
                return self.stack.pop()

        def length(self):
            return len(self.stack)

        def view(self):
            return self.stack


    s1 = Stack()
    print(s1.length())
    s1.push(10)
    print(s1.length())
    s1.push(30)
    print(s1.length())
    s1.push(50)
    print(s1.length())
    print(s1.view())
    print(s1.pop())
    print(s1.length())
    print(s1.view())
    print(s1.pop())
    print(s1.length())
    print(s1.view())
    print(s1.pop())
    print(s1.length())
    print(s1.view())
    print(s1.pop())
    print(s1.length())
    print(s1.view())

### Queue

    class Queue:
        def __init__(self):
            self.__queue = []
            self.__head = None
            self.__tail = None

        @property
        def queue(self):
            return self.__queue

        @property
        def head(self):
            return self.__head

        @property
        def tail(self):
            return self.__tail

        def push(self, value):
            if len(self.__queue) == 0:
                self.__tail = value
                self.__head = value
            else:
                self.__tail = value

            self.__queue.insert(0,value)



    if __name__ == '__main__':
        d1=Queue()
        print('Head:',d1.head)
        print('Tail:',d1.tail)
        print('queue:',d1.queue)

        d1.push_right(10)
        print('Head:',d1.head)
        print('Tail:',d1.tail)
        print('queue:',d1.queue)

        d1.push_left(-10)
        print('Head:',d1.head)
        print('Tail:',d1.tail)
        print('queue:',d1.queue)

        d1.push_left(-20)
        print('Head:',d1.head)
        print('Tail:',d1.tail)
        print('queue:',d1.queue)

        d1.push_right(20)
        print('Head:',d1.head)
        print('Tail:',d1.tail)
        print('queue:',d1.queue)

### Deque

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

### hash

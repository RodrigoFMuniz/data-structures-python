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

    def push_right(self, value):
        if len(self.__queue) == 0:
            self.__tail = value
            self.__head = value
        else:
            self.__tail = value
        
        self.__queue.append(value)


    def push_left(self, value):
        self.__queue.insert(0,value)
        self.__head = value


if __name__ == '__main__':
    q1=Queue()
    print('Head:',q1.head)
    print('Tail:',q1.tail)
    print('Queue:',q1.queue)

    q1.push_right(10)
    print('Head:',q1.head)
    print('Tail:',q1.tail)
    print('Queue:',q1.queue)

    q1.push_left(-10)
    print('Head:',q1.head)
    print('Tail:',q1.tail)
    print('Queue:',q1.queue)

    q1.push_left(-20)
    print('Head:',q1.head)
    print('Tail:',q1.tail)
    print('Queue:',q1.queue)

    q1.push_right(20)
    print('Head:',q1.head)
    print('Tail:',q1.tail)
    print('Queue:',q1.queue)

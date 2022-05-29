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
    
    def pop_queue(self):
        if len(self.__queue) == 0:
            pass
        else:
            self.__queue.pop()
            self.__head = self.__queue[-1]
        

if __name__ == '__main__':
    d1=Queue()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.push(10)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.push(-10)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.push(-20)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.push(20)
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.pop_queue()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.pop_queue()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)

    d1.pop_queue()
    print('Head:',d1.head)
    print('Tail:',d1.tail)
    print('queue:',d1.queue)


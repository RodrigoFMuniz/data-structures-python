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

q1=Queue()
print(q1.head)
print(q1.tail)
print(q1.queue)
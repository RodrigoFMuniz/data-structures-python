# Data Structures

## Using It to solve problems

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

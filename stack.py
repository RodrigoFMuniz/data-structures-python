class Stack:
    def __init__(self):
        self.stack = []
    
    def append_stack(self,item):
        self.stack.append(item)
    
    def stack_length(self):
        return len(self.stack)
    

s1 = Stack()
print(s1.stack_length())
s1.append_stack(10)
print(s1.stack_length())
s1.append_stack(30)
print(s1.stack_length())
s1.append_stack(50)
print(s1.stack_length())
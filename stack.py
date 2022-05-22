class Stack:
    def __init__(self):
        self.stack = []
    
    def append_stack(self,item):
        self.stack.append(item)
    
    def stack_length(self):
        return len(self.stack)
class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peak(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()

      
def is_balanced(exp):
    
    inside = ['[','(','{']
    out = [']',')','}']
    myStack = MyStack()
    
    for i in exp:
        if i not in out:
            myStack.push(i)
            
        if i in out:
            j = myStack.peak()
            if i == out[0] and j == inside[0]:
                return True
            
            if i == out[1] and j == inside[1]:
                return True
            
            if i == out[2] and j == inside[2]:
                return True
            
            else:
                return False
            
        

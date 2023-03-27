class Stack:  
    def __init__(self) -> None:
        self.stack=[]
    def empty(self):
        empty = False
        if len(self.stack) == 0:
            empty = True
        return empty
    def top(self):
        top = None
        if self.empty():
            pass
        else :
            top = self.stack[-1]
        return top
    def pop(self):
        pop = None
        if self.empty():
            pass
        else:
            pop = self.stack.pop()
        return pop
    def push(self, data):
        self.stack.append(data)
    def __repr__(self) -> str:
        return repr(self.items)
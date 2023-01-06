class Stack:
    def __init__(self) :
        self.list = []


    def __str__(self) -> str:
        value = self.list.reverse()
        value =  [str(x) for x in self.list]
        return '\n'.join(value)

    def Empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return 'the value is successuly inserted'

    def pop(self, value):
        if self.Empty():
            return 'the list is empty'
        else:
            self.list.pop()

    def peek(self):
        if self.Empty():
            return 'The list is empty'
        else:
            return self.list[-1]
    


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
print('-----------------')
print(stack.peek())
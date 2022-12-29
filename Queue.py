class Queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.item.append(value)
        return 'the element is add in the end of the list'
    
    def dequeue(self):
        if self.isEmpty():
            return 'the list is empty'
        else:
            return self.item.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'the list is empty '
        else:
            return self.item[0]

    
customqueue = Queue()

customqueue.enqueue(10)
customqueue.enqueue(11)
customqueue.enqueue(12)


print(customqueue.peek())
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None



class SList:
    def __init__(self) -> None:
       self.head = None
       self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next



    def insert(self,value, location):
        new = Node(value)

        if self.head == None:
            self.head = new
            self.tail = new
        else:
            if location == 0:
                new.next == self.head
                self.head = new
            elif location == 1:
                new.next = None
                self.tail.next = new
                self.tail = new
                
                

        

list = SList()

list.insert(1,1)
list.insert(2,0)

print([node.value for node in list])
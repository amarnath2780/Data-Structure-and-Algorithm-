class BinarySearch:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChil = None


def insert(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.leftChild == None:
            root.leftChild =  BinarySearch(value)
        else:
            insert(root.leftChild, value)
    elif value >= root.data:
        if root.rightChil == None:
            root.rightChil = BinarySearch(value)
        else:
            insert(root.rightChil , value)

    return 'the node is successfully created'


def traverse(root):
    if not root:
        return
    else:
        print(root.data)
        traverse(root.leftChild)
        traverse(root.rightChil)

def search(root , value):

    if root.data == value:
        print('value on root')
    elif value < root.data:
        if root.leftChild.data == value:
            print('Value at leftchild') 
        else:
            search(root.leftChild, value)
    elif value > root.data:
        if root.rightChil.data == value:
            print('Value at right Child')
        else:
            search(root.rightChil , value)

new  = BinarySearch(None)

print(insert(new,60))
print(insert(new,80))
print(insert(new,50))
print(insert(new,90))

search(new,50)


def heapify(list , n ,i ):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and list[left] < list[smallest]:
        smallest = left

    if right < n and list[right] < list[smallest]:
        smallest = right

    if smallest != i :
        list[i] , list[smallest] = list[smallest] , list[i]
        heapify(list,n,smallest)

def sort(list):
    n = len(list)
    for i in range(int(n/2)-1,-1,-1):
        heapify(list, n, i)

    for i in range(n-1,0,-1):
        list[0] , list[i] = list[i] , list[0]
        heapify(list,i,0)
    list.reverse()

list = [3,2,4,2,5,2,4,6,82,5,6,8]

sort(list)
print(list)
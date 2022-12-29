def partition(list , low , high):
    i = low - 1
    pivot = list[high]

    for j in range(low,high):
        if list[j] <= pivot:
            i+=1
            list[i] ,list[j] = list[j] ,list[i]
    list[i+1] , list[high] = list[high] , list[i+1]
    return (i+1)



def quickSort(lists, low , high):
    if low <  high:
        pi = partition(lists, low , high)
        quickSort(lists, low, pi-1)
        quickSort(lists , pi+1 , high)

lists= [2,1,7,6,5,3,4,9,8]
quickSort(lists, 0 ,len(lists)-1 )
print(lists)

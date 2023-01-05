def partion(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low,high):
        if list[j]<= pivot:
            i+=1
            list[i] , list[j] = list[j] , list[i]

    list[i+1] , list[high] = list[high] , list[i+1]

    return i+1


def quicksort(list, low , high):
    if low < high:
        pi = partion(list,low,high)
        quicksort (list , low, pi-1)
        quicksort(list , pi+1 , high)



list = [9,8,7,6,5,4,3,2,1]
quicksort(list,0,len(list)-1)

print(list)

    
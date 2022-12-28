def partion(list , low , high):
    i = low - 1
    pivot = list[high]

    for j in range(low,high):
        if list[j] <= pivot:
            i+=1
            list[i] ,list[j] = list[j] ,list[i]
    list[i+1] , list[high] = list[high] , list[i+1]
    return (i+1)

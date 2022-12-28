lists = [1,5,55,0,45,4,33,42,2,2,21,2,4,1]


for i in range(len(lists)):
    min = i

    for j in range(i+1 , len(lists)):
        if lists[j] < lists[min]:
            min = j

    if lists[i] !=  lists[min]:
        lists[i] , lists[min] = lists[min] , lists[i]


print(lists)
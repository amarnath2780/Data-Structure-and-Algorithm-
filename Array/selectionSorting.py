list = [1,3,5,6,3,2,1,4,5,-1]


for i in range(len(list)):
    min = i
    for j in range(i+1,len(list)):
        if list[j] <= list[min]:
            min = j
    
    if list[i] != list[min]:
        list[i] , list[min] = list[min] , list[i]


print(list)
def bubblesort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list [j] , list[j+1] = list[j+1] , list[j]



list = [9,6,5,4,6,3,2,5,3]


bubblesort(list)


print(list)
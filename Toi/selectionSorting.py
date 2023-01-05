def selectionSorting(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j]< list[min]:
                min = j

        list[i] , list[min] =  list[min] , list[i]


list = [1,3,2,21,41,2,4,3,51,2,4]

selectionSorting(list)


print(list)
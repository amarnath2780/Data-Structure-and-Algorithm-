list = [8,2,3,4,1,4,3,2,1,3]


for i in range(len(list)-1):
    min = i
    for j in range(i+1,len(list)):
        if list[j] < list[min]:
            min = j

    list[i] , list[min] = list[min] , list[i]


print(list)


# The time complexity of selection sort is O(N^2) 
# The space complexity of selection sort is O(1)
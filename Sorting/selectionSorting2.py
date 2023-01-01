lists = [1,5,55,0,45,4,33,42,2,2,21,2,4,1]
 
print(lists)

for i in range(len(lists)-1):
    min_value = min(lists[i:])
    min_index = lists.index(min_value,i)
    lists[i] , lists[min_index] = lists[min_index] , lists[i] 


print(lists)


# It will work even if there is duplicate elements

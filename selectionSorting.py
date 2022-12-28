lists = [1,5,55,0,45,4,33,42,2]


print(lists)

for i in range(len(lists)-1):
    min_value = min(lists[i:])
    min_index = lists.index(min_value)
    if lists[i] != lists[min_index]:
        lists[i] , lists[min_index] = lists[min_index] , lists[i]


print(lists)


# This logic will now work if the list have duplicate elemets

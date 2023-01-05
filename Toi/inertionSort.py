def insertion(list):
    for i in range(len(list)):
        key = list[i]
        j = i-1 

        while j>=0 and key < list[j]:
            list[j+1] = list[j]
            j-=1

        list[j+1] = key 

list = [2,4,2,1,2,4,6,3,2,3,66]
insertion(list)
print(list)
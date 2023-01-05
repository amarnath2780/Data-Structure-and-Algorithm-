list = [5,0,3,4,-1,2,14,2]

end = len(list)-1

for i in range(end):
    for j in range(end-i):
        if list[j] > list[j+1]:
            list[j] , list[j+1] = list[j+1] , list[j]


print(list)
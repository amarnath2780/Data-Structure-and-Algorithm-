list = [1,2,3,4,5,6]

limit = 6


for i in range(0,limit):
    num = list[0]
    for j in range(0,len(list)-1):
        list[j] = list[j+1]
    list[-1]= num



print(list)




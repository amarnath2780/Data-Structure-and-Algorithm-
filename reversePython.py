def ReverseArray(list, low ,high):

    while low < high:
        list[low] , list[high] = list[high] , list[low]
        low +=1
        high-=1
    
    str1 = ''

    print(str1.join(list))



# list = [1,2,3,4,5,6,6]
a = 'The Normal'

list  = list(a)



ReverseArray(list , 0 , len(list)-1)


# Reversing a string
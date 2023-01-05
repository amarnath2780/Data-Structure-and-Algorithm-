

def searchIndex(list,start,end,value):
    if len(list) == 0 or start > end:
        return -1


    mid = (start+end)//2

    if value == list[mid]:
        return mid
    
    if value < list[mid]:
        return searchIndex(list,start,mid-1,value)
    elif value >  list[mid]:
        return searchIndex(list,mid+1,end,value)

list = [1,2,3,4,5,22]

start = 0
end = len(list) -1
value = 22

index = searchIndex(list,start,end,value)

if index == -1:
    print('value not found')
else:
    print(f'{list[index]} in {index+1} postion')
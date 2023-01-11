name = 'WOW'

start = 0
end = len(name)-1

def palindrom(name,start,end):
    while start<end:
        if name[start] == name[end]:
            start+=1
            end+=1
        else:
            return False
        return True


print(palindrom(name,start,end))
word = '  Data Structure  Algorithm  '

lists= []

start = 0



for i in word:
    lists.append(i)
end = len(lists)-1

for i in range(len(lists)):
    if lists[i] != ' ':
        start = i
        break


for i in range(end ,0 , -1):
    if lists[i] != ' ':
        end = i
        break

list = ''
for i in range(start,end+1):
    list += lists[i]

print(list)

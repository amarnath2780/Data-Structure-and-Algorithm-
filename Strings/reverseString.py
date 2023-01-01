# Reverse a string

sting = 'Keep Coding'

final_str = ''

for i in sting:
    final_str = i + final_str

print(final_str)

# Time complexity is O(n)

list = []

for i in sting:
    list.append(i)

start = 0
end = len(list)-1

while start < end:
    list[start] , list[end] = list[end] , list[start]
    start +=1
    end -=1

final = ''

for i in list:
    final += i

print(final)
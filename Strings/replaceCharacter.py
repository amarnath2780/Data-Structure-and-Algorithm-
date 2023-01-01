
word = 'Dxtx Structure xnd xlgorithm'

list = []

for i in word:
    list.append(i)

for i in range(len(list)):
    if list[i] == 'x':
        list[i] = 'a'

string = ''

for i in list:
    string += i


print(string)


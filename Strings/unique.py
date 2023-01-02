# totoal number of unique letters in a string
string = 'hello'

x = set()

for i in string:
    x.update(i)

count = len(x)

print(count)
print(x)
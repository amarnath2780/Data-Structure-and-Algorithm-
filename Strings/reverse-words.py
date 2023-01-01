#Reverse the letters in word but keep the order

sting = 'Discipline  will take you places where motivation can\'t'


final =''
temp = ''

for i in range(len(sting)):
    if sting[i] == ' ':
        final = final + temp + " "
        temp = ''
    else:
        temp = sting[i] + temp

final = final + temp + " "

print(sting)
print(final)
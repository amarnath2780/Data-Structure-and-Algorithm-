#Reverse words order in a given string


sting = 'Discipline  will take you places where motivation can\'t'

final = ''
temp = ''

for i in range(len(sting)):
    if sting[i] != ' ':
        temp = temp + sting[i]
    else:
        final = temp + " "  +  final 
        temp = ''

final = temp  + " "+ final 

print(sting)
print(final)



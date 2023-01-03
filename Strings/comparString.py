# Compare two strings with backspace character


def  ifequal(str1,str2):
    end1 = len(str1) - 1
    end2 = len(str2) - 1

    while end1 >=0 and end2 >= 0 :
        ind1 = getChar(str1 , end1)
        ind2 = getChar(str2 , end2)

        if ind1 < 0 and ind2 < 0:
            return True
        if ind1 < 0 or ind2 < 0:
            return False
        if str1[ind1] != str2[ind2]:
            return False
        
        end1 = ind1 -1
        end2 = ind2 -1

    return True






def getChar(str, end):

    special = 0

    while end >= 0:
        if str[end] != '#':
            if special == 0:
                return end
            else:
                special -= 1
        else:
            special +=1

        end -=1

    return end




str1 = 'hee##o'

str2 = 'he#o'


print(ifequal(str1,str2))
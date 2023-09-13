

#-----------------------------------------------------------------------------------------------------
#Lowest common mutiple
#Finding Lowest common mutiple of two numbers means finding the smallest number that is a multiple of both the numbers.
#------------------------------------------------------------------------------------------------------
def Lowest_common_mutiple(number1, number2):
    if number1 > number2:
        greater = number1
    elif number2 > number1:
        greater = number2
    while(True):
        if ((greater % number1 == 0) and (greater % number2 == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

print(Lowest_common_mutiple(5, 4))
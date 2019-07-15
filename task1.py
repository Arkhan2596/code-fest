def check(year) :
    if year / 4 and year / 100 :
        return False

    elif year / 400 :
        return True

year = int(input('Enter the year to check whether its a leap year or not : '))
output = check(year)

if output == True :
    print('It is a leap year.')

elif output == False :
    print('It is not a leap year as it is not divisible by 100 or 4')
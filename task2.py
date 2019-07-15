def calculate(chickens = None, cows = None, pigs = None) :
    total = (chickens * 2) + (cows * 4) + (pigs * 4)
    return total

chickens = int(input('Enter number of chickens : '))
cows = int(input('Enter number of cows : '))
pigs = int(input('Enter number of pigs : '))
result = calculate(chickens, cows, pigs)
print('The total number of legs in your farm are', result)
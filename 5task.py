def check (first, second):
    if len(first) == len(second) : 
        return True
    else:
        return False

first = input('Enter first string : ')
second = input('Enter second string : ')
output = check(first, second)
print(output)

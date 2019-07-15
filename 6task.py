def check_pass (p) :   
    if not(len(p) >= 6 and len(p) <= 24) :
        print('The length of the pass should be between 6 tp 24 chars')

    elif not any(char.isupper() for char in p) :
        print('Your pass must contain atleast one capital letter.')
    
    elif not any(char.islower() for char in p) :
        print('Your pass must contaiin atleast one lower case letter.')
    
    elif not any(char.isdigit() for char in p) :
        print('Your pass must contain atlleast one numeral.')

    else:
        print('Password is correct.')      

p = input('Enter password : ')
check_pass(p)

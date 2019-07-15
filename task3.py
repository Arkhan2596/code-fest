def fiction() :
    print('Fiction Books : \n \
           A - Comedy \n \
           B - Comic / Graphic Novel \n \
           C - Science Fiction \n \
           D - Fantasy \n \
           E - Historical Fiction')

def nonfiction() : 
    print('Non-Fiction books : \n \
           F - History & Geography \n \
           G - Arts \n \
           H - Science & Technology \n \
           I - Other')

choice = input('Are you looking for fiction or non-fiction books?')

if choice.lower() == 'nonfiction' or choice.lower() == 'non-fiction':
    nonfiction()

elif choice.lower() == 'fiction' : 
    fiction()
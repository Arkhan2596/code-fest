num = int(input('How many names do you want to enter? '))
names = []
new_names = []
for n in range (1, num + 1):
    print('#', n)
    name = input('Enter name : ')
    names.append(name)
for name in names:
    if name not in new_names:
        new_names.append(name)
print('old list :',names,'\nnew list :', new_names)
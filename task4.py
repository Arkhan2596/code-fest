def contestants(number) :
    scores = []
    for i in range(1, number + 1) : 
        print('#',i, 'contestant')
        score = int(input('Enter score : '))
        scores.append(score)
    max_score = max(scores)
    scores.sort(reverse = True)
    print('highest score :', max_score,'\nrunner-up score :', scores[1])

number = int(input('Enter number of contestants : '))
contestants(number)
def check_votes(n):
    if n == 0 :
        print('There are no votes.')
    else:
        num = n * (1 / 2)
        votes = []
        countA = 0
        countB = 0
        countC = 0

        for i in range(1, n + 1) :
            vote = input('Who do you vote for A, B or C? ')
            votes.append(vote.lower())
        
        for v in votes :
            if v == 'a' :
                countA += 1
            elif v == 'b' :
                countB += 1
            elif v == 'c' :
                countC == 1

        if countA > countB and countA > countC and countA >= num : 
            print('A has majority votes :', countA)
        
        elif countB > countA and countB > countC and countB >= num : 
            print('A has majority votes :', countB)

        elif countC > countA and countC > countB and countC >= num : 
            print('A has majority votes :', countC)
        
        else:
            print('There are no majority votes.')
number = int(input('enter number of votes : '))
check_votes(number)
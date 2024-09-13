import random as rnd

def prisoners_dillema(player1,player2):
    if player1==1 and player2==1:
        return 3,3
    if player1==1 and player2==0:
        return 0,5 
    if player1==0 and player2==1:
        return 5,0
    if player1==0 and player2==0:
        return 1,1

class tit_for_tat():
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if opponent_history[i-1]==1:
            out=1
        if opponent_history[i-1]==0:
            out=0
        return out
    def init():
        return 1
    

class freidman:
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if 0 in opponent_history:
            return 0
        else: return 1
    def init():
        return 1

class joss:
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if rnd.random()<0.1:
            return 0    
        else:
            if opponent_history[i-1]==1:
                out=1
            if opponent_history[i-1]==0:
                out=0
            return out
            
    def init():
        return 1

class tit_for_2tats:
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if opponent_history[i-1]==1:
            out=1
        if opponent_history[i-1]==0 and opponent_history[i-2]==0:
            out=0
        return out
    def init():
        return 1
    

class grasskamp:
    pass

class name_withheld:
    pass

class random_:
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if rnd.random()<0.5:
            return 0
        else: return 1
    def init():
        if rnd.random()<0.5:
            return 0
        else: return 1

class tester:
    def strat(opponent,opponent_history,i):
        opponent_history.append(opponent)
        if i==1:
            return 0
        if i==2:
            if opponent_history[i-1]==0:
                return tester.t4t(opponent,opponent_history,i)
            if opponent_history[i-1]==1:
                return tester.odd_even(opponent,opponent_history,i)


    def t4t(opponent,opponent_history,i):
        if opponent_history[i-1]==1:
            out=1
        if opponent_history[i-1]==0:
            out=0
        return out
    def odd_even(opponent,opponent_history,i):
        if i%2==0:
            return 0
        else:
            return 1
    def init():
        return 1

player1_score,player2_score=0,0
player1=joss.init()
player2=tit_for_tat.init()
player1_history=[]
player2_history=[]

for i in range(20):
    player1=joss.strat(player2,player2_history,i)
    player2=tit_for_tat.strat(player1,player1_history,i)
    print(player1,'\t',player2)
    player1_score+=prisoners_dillema(player1,player2)[0]
    player2_score+=prisoners_dillema(player1,player2)[1]
print()
print(player1_score,'\t',player2_score)
print(player1_history)
print(player2_history)



def collatz(x):
    i=0
    print(int(x),'\t',i)
    while x!=1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        i+=1
        print(int(x),'\t',i)

# collatz(81)
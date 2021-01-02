#snake water gun game in python 
# vishwam rawal 02-0--2021

import random # use for random function
def gameWin(comp,you): #created function
   # check for TiE condition
    if comp == you:
        return None
    # check for condition if coomputer choose snake
    elif comp == 's':
        if you == 'w':
            return False #youlose
        elif you == 'g':
            return True #you win
    # check for condition if computer choose water
    elif  comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    # check for condition if computer choose gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

#print statement for user 
print("Comp Turn : Snake(s) , Water(w), Gun(g")
randNo=random.randint(1,3) #generates the random number between 1,2,3 which is stored into randNo variable
if randNo == 1: 
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
        
        
        
you = input("Your Trun : Snake(s) , Water(w) ,Gun(g)")
a = gameWin(comp,you)
print(f"Comp Choose {comp}")
print(f"You choose {you}")

if a == None: 
    print("TIE")
elif a:
    print("You Won")
else:
    print("You Lose")
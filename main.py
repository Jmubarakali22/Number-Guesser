import random
t_range=input("Enter  a number  ")
if t_range.isdigit():
    t_range=int(t_range)

    if t_range <=0:
        print("Enter the number which is grater than 0 (Zero)!!")
        quit()
else:
    print("Please enter a number")
    quit()

random_num=random.randint(0,t_range)
score=0

while(True):
    score+=1
    guess=input("make a guess: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("please enter a number ")
        continue
    if guess == random_num:
        print("you are Correct")
        break
    else:
        if guess > random_num:
            print("You were above the number")
        else:
            print("You are below the number")

print("You got it in ",score,"guesses")
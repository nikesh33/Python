import random
r = random.randint(1,20)

while(True):
    print("Guess the Number:")
    inp = int(input())
    if(inp<r):
        print("Wrong Guess,Try a Greater Number")
    elif(inp>r):
        print("Wrong Guess,Try a Lower Number")
    else:
        print("Congratulations You right Number was",inp)
        break
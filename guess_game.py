import random
num=random.randint(1,10)
attempts=0
print("lesgoooooooo")
print("all the best in guessing")
n=int(input("guess the number between 1 to 10"))
while True:
    if(n==num):
        print("well u guessed it right")
        attempts+=1
        break
    if(n!=num):
        print("sry!! but u guessed it wrong")
        print(f"the correct number is {num}")
        break

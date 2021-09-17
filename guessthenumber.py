import random
def guess_the_number(): 
    while True:
        user_number = int(input("Select a number from (1-10): "))
        random_number = random.randint(1,10)
        if user_number == random_number:
            print("Your number is {} and random number is {}, Congratulations, you guessed right".format(user_number, random_number))
            print("Press any other number not between 1-10 if u want to quit")
        elif user_number >=1 and user_number <=10:
            print("Your number is {} and random number is {}, you didn't guess correctly, try again ".format(user_number, random_number))
            print("Press any other number not between 1-10 if u want to quit")
        else:
            return "See you other time"
            break

print(guess_the_number())

import random
def rockpaperscissors():
        computer_score = 0
        user_score = 0

        while True:
            rockpaperscissors_list = ['Rock','Paper','Scissors']
            user_choice = input("Rock, Paper, Scissors: ")
            random_choice = random.choice(rockpaperscissors_list)
            
            if random_choice == user_choice:
                print("Your choice is  {} My choice is {} it's scoreless".format(random_choice, user_choice))
                print("Press another key to exit ")
            elif random_choice == 'Rock' and user_choice == 'Paper':
                user_score += 1
                print("Your choice is  {} My choice is {} You Win\nYour score {} is, My score is {}".format(user_choice, random_choice, user_score, computer_score))
                print("Press another key to exit or you can keep play")        
            elif random_choice == 'Paper' and user_choice == 'Rock':
                computer_score +=1
                print("Your choice is  {} My choice is {} You lost\nYour score {} is, My score is {}".format(user_choice, random_choice, user_score, computer_score))
                print("Press another key to exit or you can keep play")
            elif random_choice == 'Rock' and user_choice == 'Scissors':
                computer_score += 1
                print("Your choice is  {} My choice is {} You lost\nYour score {} is, My score is {}".format(user_choice, random_choice, user_score, computer_score))
                print("Press another key to exit or you can keep play")
            elif random_choice == 'Scissors' and user_choice == 'Rock':  
                user_score += 1
                print("Your choice is  {} My choice is {} You win\nYour score {} is, My score is {}".format(user_choice, random_choice, user_score, computer_score))
                print("Press another key to exit or you can keep play")
            else:
                return "See you soon."
                break
                

print(rockpaperscissors())
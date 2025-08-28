import random
def number_guessing_game():
    print("Welcome to the number guessing game !")
    print (" Try to guess the number between 1 and 100. Can you guess it ?")

    #Computer picks a number 
    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            #Take user input
            guess = int(input ("Enter your guess:"))
            attempts +=1

            if guess < secret_number:
                print("Too low! try again.")
            elif guess > secret_number:
                print("Too high! try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")  
                break
        
        except ValueError:
            print("Please enter a valid number.")

if __name__== "__main__":
    number_guessing_game()
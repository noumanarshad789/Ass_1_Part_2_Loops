# 17. Write a program that continues to ask for a number until the correct number is guessed.


correct_number = 7 

while True:

    guess = int(input("Guess the number: "))
    

    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break  
    else:
        print("Incorrect guess, try again.")

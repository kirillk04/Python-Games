import random
import time

def hangman():
    words = ['peach', 'watermelon', 'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
    chosen_word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", tries," tries remaining.")
    print("_ " * len(chosen_word))

    while tries > 0:
        guess = str(input("Enter a letter: ")).lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1
            print("You have", tries," tries remaining.")

        word_display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "

        print(word_display)

        if all(letter in guessed_letters for letter in chosen_word):    ##check each letter is there
            print("Congratulations! You guessed the word.")
            break

    if tries == 0:
        print("Game over. You ran out of tries. The word was", chosen_word, ".")

def validFeedback():
    print("1. too small   2. too big  3. just right")

    #Ask user to input feedback as an integer in 1-3, 
    feedback = int(input("Enter choice 1-3: "))

    while feedback != 1 and feedback != 2 and feedback != 3: 
        feedback = int(input("Enter choice 1-3: "))

    return feedback

def guessGame():
    #set range
    start = 0
    end = 100

    print("Pick an integer in [" + str(start) + ", " + str(end) + "] in your mind.")

    #set guess to be mid of start and end
    guess = end//2
    #set variable numGuesses to be 1
    numGuesses = 1
    
    print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")

    #call validFeedback function, put its return to feedback
    feedback = validFeedback()

    while feedback != 3: 
        if feedback == 1: #too small
            start = guess + 1 #cant be 50 so dont include it
        else: 
            end = guess - 1

        #put the mid point of start and end to guess
        guess = (start + end)//2

        numGuesses = numGuesses + 1

        if guess == start or guess == end:
           print("Guess " + str(numGuesses) + ": the answer must be", guess)
           #leave the current function 
           #by calling return statement, 
           #since we find the answer
           #and finish guess game now.
           return ()

        print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")
        
        #TODO: call validFeedback function, 
        #put its return to feedback
        feedback = validFeedback()

    #TODO: now we are outside the loop, the number is guessed
    #print out Congratulations and what the value of guess is.
    print("Congratulations! The answer is " + str(guess))

def wpm():
    text = ["The quick brown fox jumps over the lazy dog, who snoozes peacefully in the warm afternoon sun, while a gentle breeze rustles the leaves of the trees nearby.", "In a world filled with constant change and challenges, it's essential to adapt, learn, and grow, both personally and professionally, to achieve lasting success and fulfillment.", 
            "The majestic mountain range, with its snow-capped peaks glistening in the morning sun, stretches as far as the eye can see, offering breathtaking views to anyone who ventures to explore it.", "In the vast tapestry of human history, countless individuals have made significant contributions that have shaped our world and left a lasting legacy for future generations to admire and learn from."]
    sample = random.choice(text)
    correct = False
    
    print("Welcome to the Words per Minute Calculator")
    input("Please prease enter when you are ready to begin")
    start = time.time()

    print(f"Type the following text: {sample}")
    user = input("Type here: ")
    end = time.time()

    print("You took " + end + " seconds.")
    words = len(sample.split())
    minutes = end/60.0
    result = words/minutes
    print("Your Words per Minute comes out to: "+ result)


def main():
    print("What game do you want to play?")
    print("1 = Hangman     2 = Guessing Game     3 = Words per Minute")
    choice = int(input())
    if choice == 1:
        hangman()
    elif choice == 2:
        guessGame()
    elif choice == 3:
        wpm()

if __name__ == '__main__':
   main()
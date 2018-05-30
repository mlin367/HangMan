import random
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/').text
soup = BeautifulSoup(source, 'lxml')
match = soup.find('div', class_='field-item even')
wordlist = match.text.split()[95:] 
WORDLIST = [x.upper() for x in wordlist]

def main():
    print("Welcome to Hangman!")
    Word = random.choice(WORDLIST)
    print("The word you will be guessing will have {} letters!".format(len(Word)))
    guesses = 7
    guessedCorrect = []
    guessedRight = ['_'] * len(Word)
    lettersGuessed = []
    print(guessedRight)
    while guesses > 0 and '_' in guessedRight:
        answer = input("Enter your letter guess: ")
        answer = str(answer)
        while not answer.isalpha() or len(answer) != 1 or answer.upper() in lettersGuessed:
            answer = input("You need to enter a single letter/you have already guessed that letter: ")
            answer = str(answer)
        if answer.upper() in Word:
            guessedCorrect.append(answer.upper())
            lettersGuessed.append(answer.upper())
            guessedRight = [x if x in guessedCorrect else '_' for x in Word]
            print("\nYou guessed a letter correctly!")
            print("Here is the word: ", guessedRight)
            print("Letter(s) guessed: {} \n".format(lettersGuessed))
        else:
            lettersGuessed.append(answer.upper())
            guesses -= 1
            print("\nYour letter guess isn't in the word!")
            print("Letter(s) guessed: ", lettersGuessed)
            print("Guesses remaining: {}\n".format(guesses))
            print("Here is the word: ", guessedRight)
    if guesses == 0:
        print("The man is hanged! You have no more guesses.")
        print("The word was: {}".format(Word))
    else:
        print("Congratulations! You guessed all the letters correctly!: ", guessedRight)
        print("The word is, indeed, {}!".format(Word))

main()
        
    

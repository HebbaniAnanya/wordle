five_letter_words = []

"""with open("answers.txt", "r") as f:
    for line in f:
        word = line.strip().lower()
        if len(word) == 5 and word.isalpha():
            five_letter_words.append(word)

# write to new file
with open("dicti.txt", "w") as f:
    for word in five_letter_words:
        f.write(word + "\n")

print(f"Total 5-letter words: {len(five_letter_words)}")
"""

import random
from collections import Counter
def load_dictionary(filepath):
    with open(filepath,"r") as f:
        words=[line.strip() for line in f]
        return words
    
def is_valid_guess(guess,dictionary):
    return guess in dictionary
    
def evaluate(guess,answer):
    result=[""]*5
    counts=Counter(answer)

    for i in range(5):
        if guess[i]==answer[i]:
            result[i]='\033[92m'+guess[i]
            counts[guess[i]]=-1
    for i in range(5):
        if result[i]:
            continue
        if counts[guess[i]]>0:
            result[i]='\033[93m'+guess[i]
            counts[guess[i]]=-1
        else:
            result[i]='\033[0m'+guess[i]
    return "".join(result) + '\033[0m'

def wordle():
    print("Welcome to wordle! You have 5 chances to guess the word!")

    words=load_dictionary("dicti.txt")
    word=random.choice(words)
    attempt=1
    while attempt<=5:
        guess=input(f"enter guess # {attempt} :").lower()
        if len(guess)!=5:
            print("sorry it needs to be a 5-letter word")
            continue
        if guess==word:
            print("yay! you guessed it")
            break
        if is_valid_guess(guess,words):
            feedback=evaluate(guess,word)
            print(feedback)
            attempt+=1
        else:
            print("sorry invalid word!")
        
    if attempt>5:
        print(f"the word was {word}")

wordle()
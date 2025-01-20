import random

import pics


#randomly choose a word from a list of words
num_lives = 6

words = ["dog", "panda", "elephant", "sheep"]
chosen_word = random.choice(words)

print(f"The chosen word has {len(chosen_word)} letters.")
print("You have six lives left. Every incorrect guess loses one life! 😰")

#placeholder for the word  
place_holder = ""
for i in chosen_word:
    place_holder += "_"
print(place_holder)

#game loop
finished = False
guessed_letters = []


while not finished:
    print(f"*******{num_lives} lives left 😰************")
    guess = input("guess a letter: ").lower()

 # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"**********you already guessed {guess}, try again 😏********")
        

    #update the placeholder
    display = ""
    for i in chosen_word:
        if i == guess or i in guessed_letters:
            display += i
            guessed_letters.append(i)
            
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        num_lives -=1
        print(f"******* {guess} is not the correct letter, try again 🐧*********")
        if num_lives == 0:
            finished = True
            print(f"the word was {chosen_word} try again next time !!!")


# Check if the player has guessed the word
    if "_" not in display:
        finished = True
        print("Correct guess!")


    print(pics.HANGMANPICS[num_lives])
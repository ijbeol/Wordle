import random
lines = open('gave.txt').read().splitlines()
myline = random.choice(lines)
answer = myline.lower()
y = 1
counter = 0
roundNumber = 0
result = ''
feedback = ['O', 'O', 'O', 'O', 'O']
previousGuesses = list()
while True:
    guess = input('Guess a word: ').lower()
    if len(guess) != 5:
        print('Please use a five letter word..')
    elif guess not in lines:
        print("I'm sorry, I do not know that word. Please try another.. ")
    elif guess in previousGuesses:
        print("It seems like you've already guessed that. Try a new word.. ")
    else:
        if guess == answer:
                print('Congratulations! You won!')
                feedback = ['🟩', '🟩', '🟩', '🟩', '🟩']
                result = "".join(result) + "".join(feedback) + str('\n')
                print(result)
                break
        else:
            for letter in guess:
                previousGuesses.append(guess)
                if letter == answer[counter]:
                    feedback[counter] = "🟩"
                elif letter in answer:
                    feedback[counter] = "🟨"
                else:
                    feedback[counter] = "⬜"
                counter += 1
            result = "".join(result) + "".join(feedback) + str('\n')
            print(result)
            roundNumber += 1
    print('You have used {} out of 6 attempts!'.format(roundNumber))
    counter = 0
    if roundNumber == 6:
        print(myline)
        break
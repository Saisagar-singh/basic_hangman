# Write your code here
import random

print('H A N G M A N')


while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu != "play":
        break
    else:
        word = ['python', 'java', 'kotlin', 'javascript']
        r_word = random.choice(word)
        hyphen_len = '-' * (len(r_word))
        x = list(hyphen_len)
        count = 8
        typed = []
        while count > 0:
            i = 0
            print("")
            user = input(hyphen_len + '\nInput a letter: ')
            if len(user) == 1:
                if user.islower() and user.isalpha():
                    if user in typed:
                        print('You already typed this letter')
                    else:
                        if user not in r_word:
                            print('No such letter in the word')
                            count -= 1
                        elif user in x:
                            print('You already typed this letter')
                        else:
                            for letter in r_word:
                                if user == letter:
                                    x[i] = user
                                i += 1
                            hyphen_len = "".join(x)
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should input a single letter")
            typed.append(user)
            if x == list(r_word):
                break
        if x == list(r_word):
            print('You guessed the word {}!'.format(r_word))
            print('You survived!\n')
        else:
            print('You are hanged!\n')

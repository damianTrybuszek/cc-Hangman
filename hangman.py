import random, time

def hello():
    name = input("Hello, what is your name? :  ")
    print( "Hi " + name + " ! " +chr(9995))
    time.sleep(1)
    print("Let's play a game!")
    time.sleep(1)
    print("It's called hangman.")
    time.sleep(1)

def is_valid_category(category):
    return category in ["cities", "countries", "vegetables", "fruits", "animals"]

def category_choice():
    while True:
        user_input_category = input("Please choose category: cities, countries, vegetables, fruits, animals, or input quit to exit: ")
        if is_valid_category(user_input_category.lower()):
            category_list = (open("data\\" + user_input_category + ".txt", "r")).read()
            word = random.choice(category_list.split())
            return word
        elif user_input_category.lower() == "quit":
            return False
        else: 
            print("Please provide correct category")

def level_choice():
    while True:
        user_input_level_choice = input("Please choose difficult level: 1 - easy, 2 - medium, 3 - hard, or input quit to exit: ")
        if user_input_level_choice == "1":
            lives = 10
            return lives
        elif user_input_level_choice == "2":
            lives = 7
            return lives
        elif user_input_level_choice == "3":
            lives = 4
            return lives
        elif user_input_level_choice.lower() == "quit":
            return False
        else:
            print(chr(9940) + "Please choose correct diffucult level!")

def play(word, lives):
    guessed_letter_list = []
    password = list(word)
    user_word = len(password) * ["_ "]
    while True:
        print("Lives rest:", lives*chr(11088))
        print("Letter that you already choosen: " , guessed_letter_list)
        print("".join(user_word))
        letter = (input("Guess a letter: ")).lower()
        # if letter.isalpha() == False:
        if letter.isalpha()==False or len(letter) > 1 or letter == " ":
            print("You should only use a letter!")
        elif letter in guessed_letter_list:
            print("You already guessed this letter, try something else.")
        elif letter in password:
            guessed_letter_list.append(letter)
            print("Nice guess")
            for i in range(len(password)):
                if password[i] == letter:
                    user_word[i] = letter
            if user_word == password:
                print(chr(9989)*10," Congratulations! You Won! ", chr(9989)*10, "\n", word )
                break
        else:
            guessed_letter_list.append(letter)
            lives -= 1
            print("Bad choice! ", chr(9940))
            if lives == 0:
                print(chr(9940)*10, " Game over!!! ", chr(9940)*10)
                break

def again():
    while True:
        play_again = input("Play again? yes/no: ")
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            return False
        else: 
            print("Please input yes or no!")

def main():
    hello()
    while True:
        word = category_choice()
        if word == False:
            break
        lives = level_choice()
        if lives == False:
            break
        play(word, lives)
        play_again = again()
        if play_again:
            print("Play again!")
        else: 
            break

main()
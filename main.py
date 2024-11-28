from itertools import islice
import random
import os
# Traits and Characters
traits = ["Name", "Color", "Hair", "Number of Eyes", "Hat", "Nose", "Horns", "Scales", "Ears", "Fins", "Eyebrows"]
characters = [
    ["Jason", "purple", "yes", "two", "yes", "yes", "yes", "no", "no", "no", "yes"],
    ["Violet", "yellow", "no", "two", "no", "no", "no", "yes", "no", "yes", "yes"],
    ["Bernie", "orange", "no", "two", "no", "yes", "yes", "no", "no", "no", "no"],
    ["Lawrence", "blue", "no", "one", "no", "no", "no", "no", "no", "no", "no"],
    ["Edith", "green", "no", "three", "no", "no", "no", "no", "no", "no", "no"],
    ["Umberto", "purple", "no", "four", "yes", "no", "no", "no", "no", "no", "yes"],
    ["Eve", "orange", "no", "four", "no", "no", "no", "no", "no", "no", "no"],
    ["Walter", "blue", "yes", "two", "yes", "no", "no", "no", "no", "no", "no"],
    ["Telly", "purple", "no", "one", "no", "yes", "no", "no", "no", "no", "no"],
    ["Opus", "green", "no", "two", "yes", "no", "no", "no", "no", "no", "yes"],
    ["Zed", "yellow", "no", "two", "no", "no", "no", "yes", "no", "yes", "no"],
    ["Petrovo", "orange", "no", "two", "no", "no", "no", "no", "yes", "no", "no"],
    ["Richard", "green", "no", "four", "no", "no", "yes", "no", "no", "no", "no"],
    ["Celia", "purple", "yes", "four", "no", "yes", "no", "no", "no", "no", "no"],
    ["Hakem", "yellow", "no", "three", "no", "no", "no", "no", "no", "no", "no"],
    ["Boris", "blue", "no", "one", "yes", "no", "no", "no", "no", "no", "no"],
    ["Albert", "orange", "no", "one", "no", "yes", "no", "yes", "yes", "no", "yes"],
    ["Gina", "green", "yes", "three", "no", "no", "no", "no", "yes", "no", "no"],
    ["Molly", "blue", "yes", "three", "no", "no", "yes", "no", "no", "no", "yes"],
    ["Peter", "yellow", "yes", "three", "no", "no", "yes", "no", "no", "no", "yes"],
    ["Finnian", "green", "no", "one", "no", "no", "no", "no", "no", "no", "no"],
    ["Sam", "purple", "no", "two", "no", "no", "no", "no", "no", "yes", "yes"],
    ["Edgar", "blue", "no", "four", "no", "no", "no", "no", "no", "no", "no"],
    ["Quill", "orange", "no", "two", "no", "no", "no", "yes", "no", "yes", "yes"],
]
def clear(screen_title = ""):
    os.system('cls')
    os.system('clear')
    print(screen_title)
def user_input(prompt, list_section, offset = 0, limit = 0):
    for i, item in islice(enumerate(list_section), limit, None):
            print(f"{i + offset}. {item}")
    answer = input("Select a "+ prompt + ": ").strip()
    while not answer.isdigit():
        answer = input("Invalid choice. Please enter the digits of a valid " + prompt + ": ").strip()
    while int(answer) <= 0 or int(answer) >= len(list_section) + offset:
        try:
            answer = int(input("Invalid choice. Please select a valid " + prompt + ": ").strip())
        except:
            pass
    return int(answer)
secret_character = random.choice(characters) # Intialize Character
penalty_points = 0 # Intialize Points
# Instrunctions
clear("\nWelcome to the Guess Who game!")
print(f"Person: {secret_character}")
print("\n- In this game, you will try to guess the identity of a secret character.")
print("- You can ask for clues about the character by entering 1, but each clue will cost you 2 penalty points.")
print("- You can guess the character by entering 2, if you guess the character incorrectly, you will be assessed 10 penalty points.")
print("- Your goal is to guess the character with as few penalty points as possible.")
print("- You can exit by entering 2.")
input("\nPress ENTER to get started!")
while True:
    # Menu
    clear(f"Penalty Points: {penalty_points}")
    print("1. Get clues about the secret character")
    print("2. Guess the identity of the secret character")
    print("3. Exit the program")
    choice = input("Enter your choice: ").strip()
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ").strip()
    if choice == '1':
        clear("Clues Screen")
        trait_choice = user_input("trait category", traits, 0, 1)
        print("The secret character's", traits[trait_choice], "is", secret_character[trait_choice])
        penalty_points += 2 # Add 2 penatly points
        print("Penalty Points:", penalty_points) # Display Points
        input("Press ENTER to go back to the main screen.")
    elif choice == '2':
        clear("Guess Who Screen")
        guess_choice = user_input("character", [character[0] for character in characters], 1)  - 1
        if characters[guess_choice] == secret_character:
            clear()
            print("Congratulations! You correctly guessed the secret character!") 
            print("Your total penalty point score is", penalty_points)
            break # Exit
        else:
            print("Sorry, your guess was wrong.")
            penalty_points += 10 # Add 10 penatly points because of incorrect guess
            print("Penalty Points:", penalty_points) # Display Points
            input("Press ENTER to go back to the main screen.")
    elif choice == '3':
        print("Exiting the program.\nHave a good day!") # Exit Message
        break # Exit
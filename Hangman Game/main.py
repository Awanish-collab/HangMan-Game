import emoji
from random_word_generator import  random_word_selector
#print(random_word_selector())

def change_current_status_word(selected_word,input_character,current_status_word):
    modified_current_status_word = ""
    for i in range(len(selected_word)):
        if current_status_word[i] == "_" and selected_word[i] == input_character:
            modified_current_status_word += selected_word[i]
        else:#U+1F613	
            modified_current_status_word += current_status_word[i]
    return modified_current_status_word

def input_char_in_word(selected_word,input_character,current_status_word,attempts_remaining):
    if input_character in selected_word:
        current_status_word = change_current_status_word(selected_word,input_character,current_status_word)
    else:
        attempts_remaining -= 1
    return current_status_word,attempts_remaining

def print_current_state(current_status_word,attempts_remaining):
    print("Current state of word :",end=" ")
    for i in current_status_word:
        print(i,end=" ")
    print("\tAttempts remaining : {}".format(attempts_remaining))

def check_game_status(selected_word,current_status_word,attempts_remaining):
    if attempts_remaining <= 0:
        print("Sorry ! You lost your Chance",emoji.emojize(":zipper-mouth_face:"))
        print("The word was : {}".format(selected_word))
        return False
    if selected_word == current_status_word:
        print("Congratulations !! You Won",emoji.emojize(":grinning_face_with_big_eyes:"))
        return False
    return True

def play_game(attempts = 5):
    selected_word = random_word_selector()
    current_status_word = ""
    for i in selected_word:
        if i == " " or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            current_status_word += i
        else:
            current_status_word += "_"
        
    attempts_remaining = attempts
    print_current_state(current_status_word,attempts_remaining)

    while True:
        input_character = input("Guess the Character : ")
        print('')
        current_status_word,attempts_remaining = input_char_in_word(selected_word,input_character,current_status_word,attempts_remaining)
        print_current_state(current_status_word, attempts_remaining)
        game_end_checker = check_game_status(selected_word,current_status_word,attempts_remaining)
        if game_end_checker == False:
            break

if __name__ == '__main__':
    play_game()

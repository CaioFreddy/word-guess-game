import json
import random


def read_file(filename: str):
    """
    Receives name of the json file, open, read and
    returns a dict of the data
    """
    with open(filename) as file:
        raw_file = json.load(file)
    return raw_file


def get_list_names(raw_file: dict):
    """
    Get the list of characters names inside raw json file and return that list
    """
    names = [word['characterName'] for word in raw_file.get('characters')]
    return names


def play_game(words: list, max_turns: int = 5):
    print("Have fun!")

    word = random.choice(words)
    turn = 1
    shots = ''

    while turn <= max_turns:
        answer = []

        for char in word:
            if char.lower() in shots:
                answer.append(char)
            else:
                answer.append('_')

        if '_' not in answer:
            print("Congratulations! You Won!")
            print(f"The word was: {word}")
            break

        print(''.join(answer))
        shot = input("Give a shot:")
        if len(shot) > 1:
            print('Invalid input, please insert only one char!')
            shot = input("Give a shot:")
        shots += shot.lower()

        if turn == max_turns:
            print("You reached the maximum number of turns. You Lost!")
            print(f"The word was: {word}")
        else:
            print(f'You only have {max_turns - turn} turns left!')

        turn += 1


if __name__ == '__main__':
    words = get_list_names(read_file('got_characters.json'))

    wanna_play = input("Do you wanna play?\n")
    while wanna_play.lower() in ('yes', 'y'):
        play_game(words)
        wanna_play = input("Try again?\n")

    print("Ok, I'll be here if you change your mind!")

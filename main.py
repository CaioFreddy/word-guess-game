import json
import random


class Game:
    def __init__(self, word_list: list, player_name: str, max_turns: int = 10):
        self.word_list: list = word_list
        self.player_name = player_name
        self.word = None
        self.guesses: str = ''
        self.turn: int = 1
        self.max_turns: int = max_turns
        self.played_game: int = 0
        self.wins: int = 0
        print(f"Welcome {self.player_name}!\nHave fun!")

    def choose_random_word(self):
        self.word = random.choice(self.word_list)

    def check_answer(self):
        answer = []

        for char in self.word:
            if char.lower() in self.guesses:
                answer.append(char)
            elif char == ' ':
                answer.append(char)
            else:
                answer.append('_')

        if '_' not in answer:
            self.handle_result(win=True)
            print(f"The word was: {self.word}")
            return True

        print(''.join(answer))
        return False

    def handle_result(self, win: bool):
        if win:
            print("Congratulations! You Won!")
            print(f"The word was: {self.word}")
            self.wins += 1
        else:
            print("You reached the maximum number of turns.")
            self.guesses = input("Give your shot: ")
            self.check_answer()
            print("Wrong answer!")
            print(f"The word was: {self.word}")
            print()

        self.played_game += 1

    def input_guess(self):
        guess = input("Type your guess: ")
        if len(guess) > 1:
            print('Invalid input, please insert only one char!')
            guess = input("Give a shot:")
        self.guesses += guess.lower()

    def handle_turn(self):
        if self.turn == self.max_turns:
            self.handle_result(win=False)
        else:
            print(f'You only have {self.max_turns - self.turn} turns left!')
        self.turn += 1

    def reset_turn(self):
        self.turn = 1

    def play(self):
        # Choose a random word from the list  of words
        self.choose_random_word()

        while self.turn <= self.max_turns:

            # Check if the guesses at the moment are correct and finish the game if is
            if self.check_answer():
                break

            # Get the input of the guess and stores into guesses attribute
            self.input_guess()

            # Handle the turns
            self.handle_turn()
        self.reset_turn()

    def game_over(self):
        print(f"The player {self.player_name} played {self.played_game}"
              f"time(s) and have won {self.wins} time(s).")


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


if __name__ == '__main__':
    words = get_list_names(read_file('got_characters.json'))

    wanna_play = input("Do you wanna play?\n")
    print()
    player_name = input("What's your name?\n")
    game = Game(word_list=words, player_name=player_name)
    while wanna_play.lower() in ('yes', 'y'):
        game.play()
        wanna_play = input("Try again?\n")

    game.game_over()

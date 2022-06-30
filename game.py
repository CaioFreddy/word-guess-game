"""
Module with the Game Class
"""
import random
from player import Player


class Game:
    """
    Class responsible for the actions and execution of the game
    """

    def __init__(self, gamer: Player, word_list: list, max_turns: int = 10):
        """Constructor method"""
        self.player = gamer
        self.max_turns: int = max_turns
        self.choose_random_word(word_list)
        self.guesses: str = ""
        self.turn: int = 1

    def choose_random_word(self, word_list):
        """
        Chooses randomly a word inside the list and put inside the self.word attribute.
        """

        self.word = random.choice(word_list)
        hidden_name = []
        for char in self.word:
            if char == " ":
                hidden_name.append(char)
            else:
                hidden_name.append("_")
        print("The word to guess is:")
        print("".join(hidden_name))
        del hidden_name

    def check_answer(self):
        """
        Check if the answer is correct or not. If so, calls the method handle_result.
        """
        answer = []

        for char in self.word:
            if char.lower() in self.guesses:
                answer.append(char)
            elif char == " ":
                answer.append(char)
            else:
                answer.append("_")

        if "_" not in answer:
            self.handle_result(win=True)
            return True

        print("".join(answer))
        return False

    def handle_result(self, win: bool):
        """
        Handle the results based on the parameter win
        """
        if win:
            print(f"The word was: {self.word}")
            self.player.handle_result(win=True)
        else:
            print("You reached the maximum number of turns.")
            self.guesses = input("Give your shot: ").lower()
            if self.check_answer():
                return
            print("Wrong answer!")
            print(f"The word was: {self.word}")
            print()
            self.player.handle_result(win=False)

    def input_guess(self):
        """
        Responsible for get each guess and do some short rule validation.
        """
        guess = input("Type your guess: ")
        if len(guess) > 1:
            print("Invalid input, please insert only one char!")
            guess = input("Give a shot:")
        self.guesses += guess.lower()
        self.check_answer()

    def handle_turn(self):
        """
        Print how many rounds of the game the teams have left.
        Increment turn with +1 if the max_turn and turn are different.
        If max_turn and turn are the same, calls handle_result with a win=False as parameter.
        """
        if self.turn == self.max_turns:
            self.handle_result(win=False)
        else:
            print(f"You only have {self.max_turns - self.turn} turns left!")
        self.turn += 1

    def reset_turn(self):
        """
        Reset to turn 1
        """
        self.turn = 1

    def play(self):
        """Start and handle the game"""
        # Choose a random word from the list  of words

        while self.turn <= self.max_turns:

            # Check if the guesses at the moment are correct and finish the game if is
            if self.turn != 1 and self.check_answer():
                break

            # Get the input of the guess and stores into guesses attribute
            self.input_guess()

            # Handle the turns
            self.handle_turn()
        self.reset_turn()

    def game_over(self):
        """
        Print the name of the player, how many games the player played
        and how many times there were defeats of cource.
        """
        print(
            f"The player {self.player.display_player_name()} "
            f"played {self.player.display_games_played()} "
            f"time(s) and have won {self.player.display_number_of_wins()} time(s)."
        )

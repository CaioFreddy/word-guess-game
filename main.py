"""
Main file that runs the game
"""

import json
from player import Player
from game import Game


def read_file(filename: str):
    """
    Receives name of the json file, open, read and
    returns a dict of the data
    """
    with open(filename, encoding="utf-8") as file:
        raw_file = json.load(file)
    return raw_file


def get_list_names(raw_file: dict):
    """
    Get the list of characters names inside raw json file and return that list
    """
    names = [word["characterName"] for word in raw_file.get("characters")]
    return names


if __name__ == "__main__":
    words = get_list_names(read_file("got_characters.json"))
    CONTINUE_GAME = True
    name = input("What's your name?\n")
    player = Player(name=name)

    while CONTINUE_GAME:
        game_on = Game(word_list=words, gamer=player)
        game_on.play()
        if input("Try again?\n").lower() not in ("yes", "y"):
            CONTINUE_GAME = False
            game_on.game_over()

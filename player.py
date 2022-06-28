class Player:
    """
    Class responsible to manage the player
    """

    def __init__(self, name: str):
        """Constructor method"""
        self._name: str = name
        self.played: int = 0
        self.wins: int = 0
        self.greeting_player()

    def display_player_name(self):
        return self._name

    def display_games_played(self):
        return self.played

    def display_number_of_wins(self):
        return self.wins

    def greeting_player(self):
        """
        Function to send a welcome message to the player
        """
        print(f"Welcome {self.display_player_name()}!\nHave fun!\n")

    def handle_result(self, win: bool):
        """
        Handle the results based on the parameter win
        if True, print congratulations and increase the self.wins
        """
        if win:
            self.wins += 1
        self.played += 1

from typing import Dict, TypeVar

from player import Player
from shizuka import Shizuka

TypePlayer = TypeVar("TypePlayer", bound=Player)
player_dictionary: Dict[str, TypePlayer] = {"源静香": Shizuka}


class Manager:
    def __init__(self):
        self.first_player = ""
        self.second_player = ""

    def assign(self, first_player: str, second_player: str):
        self.first_player: Player = player_dictionary[first_player](is_first=True)
        self.second_player: Player = player_dictionary[second_player](is_first=False)

    def game(self):
        print(self.first_player.next_hand())
        print(self.second_player.next_hand())

from typing import Dict
from typing import TypeVar

from consequence import Consequence
from hand import Hand
from player import Player
from players.doraemon import Doraemon
from players.dorami import Dorami
from players.nobita import Nobita
from players.shizuka import Shizuka
from players.suneo import Suneo

TypePlayer = TypeVar("TypePlayer", bound=Player)
player_dictionary: Dict[str, TypePlayer] = {
    "源静香": Shizuka,
    "ドラえもん": Doraemon,
    "骨川スネ夫": Suneo,
    "野比のび太": Nobita,
    "ドラミ": Dorami,
}


class Judge:
    def __init__(self, first_player: str, second_player: str):
        self.first_player: TypePlayer = player_dictionary[first_player](is_first=True)
        self.second_player: TypePlayer = player_dictionary[second_player](is_first=False)
        self.history = []

    def game(self):
        first_hand = self.first_player.next_hand()
        second_hand = self.second_player.next_hand()
        consequence = self.judge(first_hand=first_hand, second_hand=second_hand)
        result = (first_hand, second_hand, consequence)
        self.history.append(result)

        if consequence is consequence.Win:
            self.first_player.is_won = True
            self.second_player.is_won = False
        if consequence is consequence.Lose:
            self.first_player.is_won = False
            self.second_player.is_won = True

        return first_hand, second_hand, consequence

    def get_converted_history(self):
        return [(h[0].value, h[1].value, h[2].value) for h in self.history]

    def get_result(self):
        wins = [h for h in self.history if h[-1] == Consequence.Win]
        return len(wins) / len(self.history)

    @staticmethod
    def judge(first_hand: Hand, second_hand: Hand):
        if first_hand is second_hand:
            return Consequence.Draw
        if first_hand is Hand.G:
            if second_hand is Hand.C:
                return Consequence.Win
            if second_hand is Hand.P:
                return Consequence.Lose
        if first_hand is Hand.C:
            if second_hand is Hand.P:
                return Consequence.Win
            if second_hand is Hand.G:
                return Consequence.Lose
        if first_hand is Hand.P:
            if second_hand is Hand.G:
                return Consequence.Win
            if second_hand is Hand.C:
                return Consequence.Lose

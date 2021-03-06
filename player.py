from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from random import choice

from hand import Hand


@dataclass
class Player(metaclass=ABCMeta):
    is_first: bool = True
    is_won: bool = False

    @abstractmethod
    def next_hand(self):
        hands = [x for x in Hand]
        return choice(hands)

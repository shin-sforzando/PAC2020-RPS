from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import random

from hand import Hand


@dataclass
class Player(metaclass=ABCMeta):
    is_first: bool

    @abstractmethod
    def next_hand(self):
        hands = [x for x in Hand]
        return random.choice(hands)

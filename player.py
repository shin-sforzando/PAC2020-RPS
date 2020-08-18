from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Player(metaclass=ABCMeta):
    is_first: bool

    @abstractmethod
    def next_hand(self):
        return "グー"

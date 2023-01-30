# 객체 (object)로 블랙잭 카드 게임 만들기

import random


class CardDeck(object):
    """A Blackjack card."""
    def __init__(self, face, suit):
        # assert face in FACES and suit in SUITS
        self.face = face
        self.suit = suit
        # print(face, suit)

    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]:
            article = "an "
        return (article + str(self.face) + " of" + self.suit)


class Dealer(object):
    """A deck of cards."""
    def __init__(self):
        "Create a deck of 52 cards and shuffle them."
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(CardDeck(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop()

    def talk(self):
        """user와 대화하기"""
        pass


class Player(object):
    """게임을 지속할건지 끝낼건지 결정"""
    pass


if __name__ == '__main__':
    FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    num_players = 1
    num_cards = 52
    deck = CardDeck(FACES, SUITS)
    deal_game = Dealer()


# 객체 (object)로 블랙잭 카드 게임 만들기

import random


class Card(object):
    """카드덱 만들기"""
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        # print(face, suit)


class Dealer(object):
    """딜러로서 게임 진행하기"""
    def __init__(self):
        """카드 섞기"""
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(CardDeck(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        """맨 위의 카드 뽑기"""
        return self.cards.pop()

    def talk(self):
        """user와 대화하기"""
        pass


class Player(object):
    """플레이어로서 게임 진행 및 종료 결정"""
    pass


if __name__ == '__main__':
    FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    num_players = 1
    num_cards = 52
    deck = CardDeck(FACES, SUITS)
    deal_game = Dealer()


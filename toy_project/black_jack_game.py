# 객체 (object)로 블랙잭 카드 게임 만들기

import random


class Card(object):
    """카드덱 만들기"""

    def __init__(self):
        self.face = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        self.suit = ['♠', '♥', '♦', '♣']

    def shuffle(self):
        cards = []
        for suit_ in self.suit:
            for face_ in self.face:
                cards.append([suit_, face_])
        random.shuffle(cards)
        print(cards)

    def draw_card(self):
        pass
    def reset(self):
        pass


class Dealer(object):
    """딜러로서 게임 진행하기"""
    def __init__(self):
        """카드 섞기"""
        pass

    # def draw(self):
    #     """맨 위의 카드 뽑기"""
    #     return self.cards.pop()

    def talk(self):
        """user와 대화하기"""
        pass


class Player(object):
    """플레이어로서 게임 진행 및 종료 결정"""
    pass


class Game(object):
    """player와 dealer에게 덱 할당시키고 loop문으로 게임 플레이"""
    def hit(self):
        pass
    def stand(self):
        pass
    def play_game(self):
        pass


if __name__ == '__main__':
    deck = Card()
    print(deck.shuffle())




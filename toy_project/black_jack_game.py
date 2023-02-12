import random
from dataclasses import dataclass

SUIT = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
FACE = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {face: value for (face, value) in zip(FACE, range(2, 11))}
VALUES.update({'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11})


class CardDeck:
    """카드덱 만들기"""
    def __init__(self):
        self.deck = self.__setup_cards()

    def __setup_cards(self):
        cards = []
        for suit in SUIT:
            for face in FACE:
                cards.append([suit, face])
        return cards

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        single_card = self.deck.pop()
        print(single_card)
        return single_card


@dataclass
class CardValue:
    face: tuple
    suit: tuple
    value: dict

    def get_value(self, add_card):
        return self.value[add_card[1]]


class Dealer:
    """딜러"""
    def __init__(self, card_value):  # 더블언더바 = dunder
        self.dealer_cards = []
        self.value = 0
        self.card_value = card_value

    def add_card(self, card):
        self.dealer_cards.append(card)
        self.value += self.card_value.get_value(card)
        print("dealer:", self.value)

    def own_card(self):
        return self.dealer_cards


class Player:
    """플레이어"""
    def __init__(self, card_value):  # 더블언더바 = dunder
        self.players_cards = []
        self.value = 0
        self.card_value = card_value

    def add_card(self, card):
        self.players_cards.append(card)
        self.value += self.card_value.get_value(card)
        print("player:", self.value)

    def own_card(self):
        return self.players_cards


# player is game이 아니므로 상속 X
# Game has player 은 ok
class Game:
    """player와 dealer에게 덱 할당시키고 loop문(play())으로 게임 플레이"""
    def __init__(self, card, player, dealer):  # main 함수의 인스턴스 넘겨받음, 밖에서 선언해야 종속성을 줄일 수 있음 ex. 고스톱 카드로 변경 가능
        self.value = 0
        self.card = card
        self.player = player
        self.dealer = dealer

    def hit(self):
        self.player.add_card(self.card.draw_card())

    # TODO: 처음 stand가 실행 될 때 dealer에게 카드 한 장이 추가로 지급되어야함
    def stand(self):
        self.dealer.add_card(self.card.draw_card())

    def burst(self):
        if self.player.value > 21:
            print('player burst!')
            exit()
        elif self.dealer.value > 21:
            print('dealer burst!')
            exit()

    def setup_play(self):
        deck = CardDeck()
        deck.shuffle()

        # 게임 시작시 player에게 두 장의 카드를, 딜러에게는 한 장의 카드를 지급
        self.player.add_card(deck.draw_card())
        self.player.add_card(deck.draw_card())
        self.dealer.add_card(deck.draw_card())

    def play(self):
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            Game.hit(self)
            Game.burst(self)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            Game.stand(self)
            Game.burst(self)

        else:
            print("Sorry, please try again.")


if __name__ == '__main__':
    card_value = CardValue(FACE, SUIT, VALUES)
    game = Game(player=Player(card_value), card=CardDeck(), dealer=Dealer(card_value))
    game.setup_play()
    while True:
        game.play()

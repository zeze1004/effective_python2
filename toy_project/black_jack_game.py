import random

SUIT = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
FACE = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


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
        # print(self.deck)

    def draw_card(self):
        single_card = self.deck.pop()
        print(single_card)
        return single_card


class Dealer(object):
    """딜러"""
    def __init__(self):  # 더블언더바 = dunder
        self.dealer_cards = []
        self.value = 0

    def add_card(self, card):
        self.dealer_cards.append(card)
        self.value += VALUES[self.dealer_cards[-1][1]]
        # TODO: 점수 출력 기능 구현
        print("dealer:", self.value)

    def own_card(self):
        return self.dealer_cards


class Player(object):
    """플레이어"""
    def __init__(self):  # 더블언더바 = dunder
        self.players_cards = []
        self.value = 0

    def add_card(self, card):
        self.players_cards.append(card)
        self.value += VALUES[self.players_cards[-1][1]]
        print("player:", self.value)

    def own_card(self):
        return self.players_cards


# player is game이 아니므로 상속 X
# Game has player 은 ok
class Game:
    """player와 dealer에게 덱 할당시키고 loop문으로 게임 플레이"""

    def __init__(self, card, player, dealer):  # main 함수의 인스턴스 넘겨받음, 밖에서 선언해야 종속성을 줄일 수 있음 ex. 고스톱 카드로 변경 가능
        self.value = 0
        self.card = card
        self.player = player
        self.dealer = dealer

    def hit(self):
        self.player.add_card(self.card.draw_card())

    def stand(self):
        self.dealer.add_card(self.card.draw_card())

    def play(self):
        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                Game.hit(self)  # hit() function defined above

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                Game.stand(self)

            else:
                print("Sorry, please try again.")
                continue
            break


if __name__ == '__main__':
    # DI <- Dependency Injection
    deck = CardDeck()
    deck.shuffle()

    # 카드 두 장 지급
    player = Player()
    dealer = Dealer()
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())

    game = Game(player=player, card=deck, dealer=dealer)
    game.hit()
    while True:
        game.play()

        if player.value > 21:
            print('player burst!')
            exit()
        if dealer.value > 21:
            print('dealer burst!')
            exit()

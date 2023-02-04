# 객체 (object)로 블랙잭 카드 게임 만들기

import random


class Card(object):
    """카드덱 만들기"""
    def __init__(self):
        self.face = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        self.suit = ['♠', '♥', '♦', '♣']
        self.deck = []

    def shuffle(self):
        for suit_ in self.suit:
            for face_ in self.face:
                self.deck.append([suit_, face_])
        random.shuffle(self.deck)
        # print(self.deck)

    def draw_card(self):
        single_card = self.deck.pop()
        print(single_card)
        return single_card

    # def reset(self):
    #     pass


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
    def __init__(self):
        self.players_cards = []
        self.value = 0
        # self.aces = 0

    def add_card(self, card: list):
        self.players_cards.append(card)
        # print(self.players_cards)
        # self.value += values[card.rank]

    def own_card(self):
        return self.players_cards


class Game(object):
    """player와 dealer에게 덱 할당시키고 loop문으로 게임 플레이"""
    def __init__(self):
        self.value = 0
        # self.aces = 0

    def hit(self):
        player_hit = Player
        card_hit = Card
        player_hit.add_card(card_hit.draw_card(self))
        print("hit")


    def hit_or_stand(self, hand):
        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                Game.hit(self)  # hit() function defined above

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False

            else:
                print("Sorry, please try again.")
                continue
            break

    # def show_some(player, dealer):
    #     print("\nDealer's Hand:")
    #     print(" <card hidden>")
    #     print('', dealer.cards[1])
    #     print("\nPlayer's Hand:", *player.cards, sep='\n ')
    #
    # def show_all(player, dealer):
    #     print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    #     print("Dealer's Hand =", dealer.value)
    #     print("\nPlayer's Hand:", *player.cards, sep='\n ')
    #     print("Player's Hand =", player.value)
    #
    # # functions to handle end of game scenarios
    #
    # def player_busts(player, dealer, chips):
    #     print("Player busts!")
    #     chips.lose_bet()
    #
    # def player_wins(player, dealer, chips):
    #     print("Player wins!")
    #     chips.win_bet()
    #
    # def dealer_busts(player, dealer, chips):
    #     print("Dealer busts!")
    #     chips.win_bet()
    #
    # def dealer_wins(player, dealer, chips):
    #     print("Dealer wins!")
    #     chips.lose_bet()
    #
    # def push(player, dealer):
    #     print("Dealer and Player tie! It's a push.")


if __name__ == '__main__':
    deck = Card()
    deck.shuffle()
    game = Game()
    # single_card__ = deck.draw_card()
    # game.add_card(single_card)

    # 카드 두 장 지급
    player = Player()
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())

    while True:
        game.hit_or_stand(player.own_card())




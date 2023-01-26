# 랜덤한 포커카드를 반환하는 제너레이터 만들기
import random


class Counter:
    def __init__(self, start, end):
        self.card = ['color_joker', 'black_joker']
        self.shape = ['♠', '♥', '♦', '♣']
        self.card_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
        for i in self.shape:
            for j in self.card_num:
                self.card.append(i + j)

        random.shuffle(self.card)

        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            print(self.num, self.card[self.num - 1])
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':
    # 클래스 호출
    c1 = Counter(1, 54)
    obj = iter(c1)
    try:
        while True:  # Print till error raised
            next(obj)
            pass
    except:
        # when StopIteration raised, Print custom message
        print("\nGAME OVER")

# 랜덤한 포커카드를 반환하는 제너레이터 만들기
import random


class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            print(self.num, card[self.num])
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':
    shape = ['♠', '♥', '♦', '♣']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'A', 'J', 'Q']
    card = ['color_joker', 'black_joker']

    # 카드덱 만들기
    for i in shape:
        for j in num:
            card.append(i + j)

    random.shuffle(card)
    # print(card)

    # 클래스 호출
    c1 = Counter(1, 54)
    obj = iter(c1)
    try:
        while True: # Print till error raised
            next(obj)
            pass
    except:
        # when StopIteration raised, Print custom message
        print("\nGAME OVER")


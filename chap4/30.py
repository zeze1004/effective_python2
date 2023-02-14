address = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.'

def index_words_iter(text):
    if text:
        print(1)
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            print(2)
            yield index + 1

it = index_words_iter(address)
print(next(it))
print(next(it))

# result = list(index_words_iter(address))
# print(result[:10])
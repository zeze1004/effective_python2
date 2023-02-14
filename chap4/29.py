stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size
#
# result = {}
# for name in order:
#   count = stock.get(name, 0)
#   print(count)
#   batches = get_batches(count, 8)
#   if batches:
#     result[name] = batches
#
# print(result)

# found = {name: get_batches(stock.get(name, 0), 8) for name in order if get_batches(stock.get(name, 0), 8)}
# print(found)

# found = {name: batches for name in order if (batches := get_batches(stock.get(name, 0), 8))}
# print(found)

# result = {name: tenth for name, count in stock.items()
#           if (tenth := count // 10) > 0}
# print(result)

for count in stock.values():  # Leaks loop variable
    print(count)
print(f'Last item of {list(stock.values())} is {count}')
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

# log('My numbers are', [1, 2])
# log('Hi there')


favorites = [7, 33, 99]
log('Favorite colors', *favorites)

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 2
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


# Example 3
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# Example 4
it = read_visits('my_numbers.txt')
print(it, list(it))
percentages = normalize(it)
print(percentages)


# Example 5
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted
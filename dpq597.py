RANGE_LIMIT = 100


def simple_generator():
    yield 1
    yield 2


print(next(simple_generator()))
print(next(simple_generator()))


def find_divisible_numbers(limit):
    return [number for number in range(1, limit + 1) if number % 3 == 0 and number % 5 == 0]


divisible_numbers = find_divisible_numbers(RANGE_LIMIT)
print('Numbers from 1 to 100 divisible by both 3 and 5:')
print(divisible_numbers)
print(f'Total count: {len(divisible_numbers)}')

start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))


def sum_range(start, end):
    return sum(range(start, end + 1))


summa = sum_range(start, end)
print(f'The sum of all numbers from {start} to {end} is: {summa}')

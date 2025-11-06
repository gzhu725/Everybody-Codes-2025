with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

gears = list(map(int, lines))

first = gears[0]
last = gears[-1]
turns = 2025 * (first / last)
print(int(turns))
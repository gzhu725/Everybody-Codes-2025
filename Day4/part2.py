with open('input.txt') as reader:
  lines = line.strip() for line in reader.readlines()

gears = list(map(int, lines))

first = gears[0]
last = gears[-1]
x = 10000000000000 / ((first / last))
print(int(x))
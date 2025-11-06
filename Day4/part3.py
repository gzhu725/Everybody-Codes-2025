import math
with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]


turns = 0
total = 0
one = None
two = None

gears = list()
for item in lines:
    if '|' in item:
        a, b = item.split('|')
        gears.extend([a, b])
    else:
        gears.append(item)

gears = list(map(int, gears))

total = 1
for i in range(0,len(gears) - 1, 2):
    curr = gears[i]
    next = gears[i+1]

    turns = (curr/next)
    total *= turns 

print(int(100 * total))


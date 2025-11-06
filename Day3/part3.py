from collections import Counter
with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

crates = list(map(int, lines[0].split(',')))
frequency = Counter(crates)

print(max(frequency.values()))


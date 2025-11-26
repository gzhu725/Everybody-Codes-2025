
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

blocks = list(map(int, lines[0].split(',')))

cols = [0] * 90
for b in blocks:
    for c in range(b - 1, len(cols), b):
        cols[c] += 1

print(sum(cols))
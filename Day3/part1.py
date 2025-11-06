with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

crates = list(map(int, lines[0].split(',')))
crates = (sorted(crates, reverse=True))

res = []
for i in range(len(crates) - 1):
    # stop at second to last
    if crates[i] == crates[i+1]:
        continue
    else:
        res.append(crates[i])

if crates[len(crates) - 1] != crates[len(crates) - 2]:
    res.append(crates[len(crates) - 1])
print(sum(res))




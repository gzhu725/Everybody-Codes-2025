with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

crates = list(map(int, lines[0].split(',')))
crates = (sorted(crates))

res = []
for i in range(len(crates) - 1):
    # stop at second to last
    if crates[i] == crates[i+1]:
        continue
    else:
        res.append(crates[i])
    
    if len(res) == 20:
        break
print(sum(res))



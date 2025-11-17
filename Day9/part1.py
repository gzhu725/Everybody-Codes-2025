with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

one = lines[0].split(':')[1]
two = lines[1].split(':')[1]
child = lines[2].split(':')[1]

res1 = 0
res2 = 0
for i in range(len(one)):
    if child[i] == one[i]:
        res1 += 1
    if child[i] == two[i]:
        res2 += 1

print(res1 * res2)
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

names = lines[0]
rules = lines[2:]
d = dict()
for r in rules:
    letter, other = r.split('>')
    other = other.strip().split(',')
    d[letter.strip()] = other 


names = names.split(',')
res = 0
for i, name in enumerate(names):
    good = True
    for c in range(len(name) - 1):
        curr = name[c]

        next = name[c+1]

        if curr not in d or next not in d[curr]:
            # print(name)
            good = False
    if good:
        print(name)
        res += (i + 1)
              

print(res)  
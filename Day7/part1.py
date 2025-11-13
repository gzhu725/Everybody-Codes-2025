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
for name in names:
    good = True
    for i in range(len(name) - 1):
        curr = name[i]

        next = name[i+1]

        if curr in d and next in d[curr]:
            # good 
            print('good')
            continue 
        else:
            # print(name)
            good = False
    if good:
        print(name)
        break        
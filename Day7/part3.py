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

def generate(prefix, rules, min_len=7, max_len=11, seen=None):
    if seen is None:
        seen = set()
    if len(prefix) >= min_len:
        seen.add(prefix)
    if len(prefix) >= max_len:
        return seen

    last = prefix[-1]
    if last not in rules:
        return seen

    for nxt in rules[last]:
        generate(prefix + nxt, rules, min_len, max_len, seen)

    return seen

total = set()
for prefix in names:
    # check if prefix itself is valid under rules before expanding
    valid = True
    for c1, c2 in zip(prefix, prefix[1:]):
        if c1 not in d or c2 not in d[c1]:
            valid = False
            break
    if not valid:
        continue

    
    total |= generate(prefix, d)

print(len(total))  # → 1154
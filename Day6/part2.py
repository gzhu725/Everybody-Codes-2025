with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

line = lines[0]
d = dict() # a: ____, b: ___, c ___
d['a'] = 0 
d['b'] = 0 
d['c'] = 0

res = 0
for i in range(len(line)):
    curr = line[i]
    
    if curr == 'a' or curr == 'b' or curr == 'c':
        before = line[0: i]
        for b in before: 
            if abs(ord(b) - ord(curr)) == 32:
                d[curr] += 1
    else:
        continue
    
print(sum(d.values()))




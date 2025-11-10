with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

line = lines[0]
l = ""
for char in line:
    if char == 'A' or char == 'a':
        l += char 

res = 0
for i in range(len(line)):
    curr = line[i]
    
    if curr == 'a':
        before = line[0: i]
        for b in before: 
            if b == 'A':
                res += 1
    else:
        continue
    
print(res)




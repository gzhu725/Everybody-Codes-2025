with open('input1.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

names = lines[0].split(',')
moves = lines[2].split(',')

# cur_index = 0 
for move in moves: 
    dir = move[0]
    num = move[1:]
    cur_index = 0
    if dir == 'L':
        cur_index -= int(num)
    else:
        cur_index += int(num)
    
    wrap = (cur_index + len(names)) % len(names)
    
    # swap
    
    temp = names[0]
    # print(temp, names[wrap], names)
    names[0] = names[wrap]
    names[wrap] = temp
print(names[0])
        
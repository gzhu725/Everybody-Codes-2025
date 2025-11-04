with open('input1.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

names = lines[0].split(',')
moves = lines[2].split(',')

cur_index = 0 
for move in moves: 
    dir = move[0]
    num = move[1:]
    if dir == 'L':
        cur_index -= int(num)
    else:
        cur_index += int(num)
    
    wrap = (cur_index + len(names)) % len(names)
print(names[wrap])
            
# wrapped_index = (index_to_access % array_length + array_length) % array_length
# wrapped_index = (index_to_access % array_length + array_length) % array_length

# print(names[cur_index])
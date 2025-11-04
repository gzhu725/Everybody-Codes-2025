with open('input1.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

names = lines[0].split(',')
moves = lines[2].split(',')

cur_index = 0 
for move in moves: 
    dir = move[0]
    num = move[1]
    if dir == 'L':
        cur_index -= int(num)
        if cur_index < 0:
            cur_index = 0
    else:
        cur_index += int(num)
        if cur_index >= len(names):
            cur_index = len(names) - 1
print(names[cur_index])
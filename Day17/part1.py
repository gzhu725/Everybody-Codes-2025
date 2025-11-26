with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

grid = []

for l in lines:
    grid.append(list(l))

def in_range(volcano, point, radius):
    # returns bool
    # (x,y)
    return (volcano[0] - point[0]) ** 2 + (volcano[1] - point[1]) ** 2 <= radius ** 2


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            vr = r
            vc = c 

res  = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != '@' and in_range((vr, vc), (r,c), 10):
            res += int(grid[r][c])

print(res)

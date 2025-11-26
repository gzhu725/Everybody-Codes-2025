with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

grid = []

for l in lines:
    grid.append(list(l))

def in_range(volcano, point, radius):
    # returns bool at that layer 
    # (x,y)
    return (radius - 1) ** 2 < (point[0] - volcano[0]) ** 2 + (point[1] - volcano[1]) ** 2 <= radius ** 2


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            vr = r
            vc = c 

most = (0,0)

for radius in range(1, len(grid) * 2):
    total = 0
    for r, row in enumerate(grid):
        for c, num in enumerate(row):
           if grid[r][c] != "@" and in_range((vr,vc), (r,c), radius):
                total += int(num)
    most = max(most, (total, radius))

print(most[0] * most[1])

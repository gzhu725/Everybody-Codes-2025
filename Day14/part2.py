with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]
lol = []
for l in lines:
    lol.append(list(l))
grid = lol

DIAG = [(1,1), (-1,-1), (-1,1), (1,-1)]
res = 0
for _ in range(2025):
    new_grid = [row[:] for row in grid]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            curr = grid[r][c]
            count = 0
            for d in DIAG: 
                if 0 <= r + d[0] < len(grid) and 0 <= c + d[1] < len(grid[0]):
                    if grid[r + d[0]][c + d[1]] == '#':
                        count += 1
            if count % 2 == 0 and curr == '#':
                new_grid[r][c] = '.'
            elif count % 2 == 0 and curr == '.':
                new_grid[r][c] = '#'
    grid = new_grid

    s = 0
    for r in grid:
        for c in r:
            if c == '#':
                s += 1
    res += s

print(res)




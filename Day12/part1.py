from collections import deque

with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

def destroyed_count(grid_lines):
    if not grid_lines: 
        return 0
    h = len(grid_lines)
    w = len(grid_lines[0])
    grid = []
    for line in grid_lines:
        r = []
        for c in line:
            r.append(c)
        grid.append(r)

    start = (0, 0)
    visited = list()
    for line in grid_lines:
        visited.append([False] * w)

    q = deque([start])

    visited[start[0]][start[1]] = True
    count = 1

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if grid[ny][nx] <= grid[y][x]:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    count += 1
    return count

print(destroyed_count(lines))

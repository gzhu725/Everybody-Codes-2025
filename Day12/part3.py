from collections import deque

with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

def flood_fill(grid, alive, starts):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    q = deque()

    destroyed = set()

    # Initialize queue
    for (x, y) in starts:
        if alive[y][x]:
            visited[y][x] = True
            q.append((x, y))
            destroyed.add((x, y))

    # 4 directions
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()
        v = grid[y][x]

        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h:
                if alive[ny][nx] and not visited[ny][nx]:
                    # Rule: can ignite equal or smaller barrel
                    if grid[ny][nx] <= v:
                        visited[ny][nx] = True
                        q.append((nx, ny))
                        destroyed.add((nx, ny))

    return destroyed

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

    alive = list()
    for line in grid_lines:
        alive.append([True] * w)
    
    starts = list() 

    def first():
        res = None
        best_count = -1
        for y in range(h):
            for x in range(w):
                if alive[y][x]:
                    destroyed = flood_fill(grid, alive, [(x,y)] )
                    count = len(destroyed)
                    if count > best_count:
                        best_count = count
                        res = (x, y)
        return res, best_count
    
    for _ in range(3):
        pos, cnt = first()
        starts.append(pos)

        destroy = flood_fill(grid, alive, [pos])
        for (x,y) in destroy:
            alive[y][x] = False 
    
    alive_final = [[True]*w for _ in range(h)]
    destroyed_final = flood_fill(grid, alive_final, starts)

    return len(destroyed_final), starts
        

final_count, s = destroyed_count(lines)
print(final_count)

with open("input.txt") as f:
    target = [list(line.strip()) for line in f.readlines()]

grid = [['.' for _ in range(34)] for _ in range(34)]

H = len(grid)
W = len(grid[0])
PH = len(target)
PW = len(target[0])

r0 = (H - PH) // 2
c0 = (W - PW) // 2

DIAG = [(1,1),(1,-1),(-1,1),(-1,-1)]

def next_grid(g):
    H = len(g)
    W = len(g[0])
    ng = [row[:] for row in g]
    for r in range(H):
        for c in range(W):
            cnt = 0
            for dr,dc in DIAG:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if g[nr][nc] == '#':
                        cnt += 1
            if g[r][c] == '#':
                ng[r][c] = '#' if cnt % 2 == 1 else '.'
            else:
                ng[r][c] = '#' if cnt % 2 == 0 else '.'
    return ng

def freeze(g):
    return tuple("".join(row) for row in g)

def extract_center(g):
    return tuple("".join(row[c0:c0+PW]) for row in g[r0:r0+PH])

# cycle detection storage
seen = {}          
match_values = []  

round_idx = 0
frozen = freeze(grid)

while frozen not in seen:
    seen[frozen] = round_idx

    # check if center matches
    if extract_center(grid) == freeze(target):
        active = sum(c == '#' for row in grid for c in row)
        match_values.append((round_idx, active))

   
    grid = next_grid(grid)
    frozen = freeze(grid)
    round_idx += 1

cycle_start = seen[frozen]
cycle_end = round_idx
cycle_len = cycle_end - cycle_start

# separate matches
pre = []
cycle = []

for idx, val in match_values:
    if idx < cycle_start:
        pre.append(val)
    else:
        cycle.append((idx - cycle_start, val))

TOTAL = 1_000_000_000

answer = 0


for idx, val in pre:
    if idx < TOTAL:
        answer += val

cycle_vals = [v for (_, v) in cycle]

if TOTAL > cycle_start:
    remaining = TOTAL - cycle_start
    full = remaining // cycle_len
    extra = remaining % cycle_len

    answer += full * sum(cycle_vals)

    for rel_idx, val in cycle:
        if rel_idx < extra:
            answer += val

print(answer)

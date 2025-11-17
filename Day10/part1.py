from collections import deque

with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]
board = lines

def count_reachable_sheep(board, max_moves=4):
    H = len(board)
    W = len(board[0])

    for r in range(H):
        for c in range(W):
            if board[r][c] == 'D':
                start = (r, c)
                break

    # BFS
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    sheep_count = 0

    while queue:
        r, c, dist = queue.popleft()

        if dist == max_moves:
            continue

        for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

                if board[nr][nc] == 'S':
                    sheep_count += 1

    return sheep_count

print(count_reachable_sheep(board, max_moves=4))

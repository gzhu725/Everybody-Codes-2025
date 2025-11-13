from itertools import combinations


with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

# WHAT THE HECK IS THIS? 


nums = list(map(int, lines[0].split(',')))

def arc_contains(a, b, c, N):
    if a == b: return False
    length = (b - a) % N
    pos = (c - a) % N
    return 0 < pos < length

def chords_intersect(a,b,c,d,N):
    if a==c or a==d or b==c or b==d:
        return False
    return (arc_contains(a,b,c,N) ^ arc_contains(a,b,d,N)) and (arc_contains(c,d,a,N) ^ arc_contains(c,d,b,N))

def best_cut(N, seq):
    s = [x-1 for x in seq]
    segments = [(s[i], s[i+1]) for i in range(len(s)-1)]
    best = None  # (count, a,b)
    for a,b in combinations(range(N), 2):
        count = 0
        for (c,d) in segments:
            if (a==c and b==d) or (a==d and b==c):
                count += 1
            elif chords_intersect(a,b,c,d,N):
                count += 1
        if best is None or count > best[0]:
            best = (count, a, b)
    # return 1-based nail indices for clarity
    return best[0], best[1]+1, best[2]+1

print(best_cut(8, nums))
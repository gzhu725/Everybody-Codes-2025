
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

### I needed help for parts 2 and 3..did not make the global ranking as a result.


nums = list(map(int, lines[0].split(',')))
def count_knots(N, seq):
    """N: number of nails (int)
       seq: list of nail numbers (1-based)
       returns total number of knots (int) and list of per-step knot counts
    """
    # convert to 0-based indices
    s = [x-1 for x in seq]
    def arc_contains(a, b, c):
        # True if c is strictly on clockwise open arc from a to b
        if a == b: 
            return False
        length = (b - a) % N
        pos = (c - a) % N
        return 0 < pos < length

    def chords_intersect(a,b,c,d):
        # exclude touching at endpoints
        if a==c or a==d or b==c or b==d:
            return False
        # proper intersection iff endpoints are interleaved on circle
        return (arc_contains(a,b,c) ^ arc_contains(a,b,d)) and (arc_contains(c,d,a) ^ arc_contains(c,d,b))

    segments = []  # list of (u,v) 0-based segments added so far
    knots_per_step = []
    total = 0
    for i in range(len(s)-1):
        u, v = s[i], s[i+1]
        new_seg = (u, v)
        knots_here = 0
        for prev in segments:
            if chords_intersect(u, v, prev[0], prev[1]):
                knots_here += 1
        segments.append(new_seg)
        knots_per_step.append(knots_here)
        total += knots_here
    return total, knots_per_step

total_knots, steps = count_knots(256, nums)
print(total_knots)
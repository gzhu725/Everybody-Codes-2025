def expand_range(r):
    a, b = map(int, r.split('-'))
    return list(range(a, b + 1))

def build_wheel_with_ranges(ranges):
    wheel = ['1']

    left_side = []   
    right_side = [] 

    for i, r in enumerate(ranges):
        nums = expand_range(r)

        if i % 2 == 0:   
            right_side.extend(str(n) for n in nums)
        else:            
            left_side.extend(str(n) for n in nums)

    wheel = left_side[::-1] + wheel + right_side
    return wheel


def rotate_and_get(wheel, turns):
    size = len(wheel)
    start = wheel.index('1')
    idx = (start + turns) % size
    return wheel[idx]


# ---- Read input ranges ----
with open("input.txt") as f:
    ranges = [line.strip() for line in f]

wheel = build_wheel_with_ranges(ranges)

turns = 202520252025
answer = rotate_and_get(wheel, turns)

print(answer)

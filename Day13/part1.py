with open('input.txt') as f:
    nums = [int(line.strip()) for line in f]


def build_wheel(nums):
    wheel = ['1']

    left_side = []
    right_side = []

    for i, n in enumerate(nums):
        if i % 2 == 0:   
            right_side.append(str(n))
        else:           
            left_side.append(str(n))

    return left_side[::-1] + wheel + right_side


def rotate_clockwise(wheel, steps):
    size = len(wheel)
    idx_1 = wheel.index('1')
    final_idx = (idx_1 + steps) % size
    return wheel[final_idx]


wheel = build_wheel(nums)

result = rotate_clockwise(wheel, 2025)

print(result)

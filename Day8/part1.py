with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

nums = list(map(int, lines[0].split(',')))
dist = 16 # for it to be in the center

res = 0
for i in range(len(nums) - 1):
    curr = nums[i]
    next = nums[i+1]
    if abs(curr - next) == dist:
        res += 1

print(res)

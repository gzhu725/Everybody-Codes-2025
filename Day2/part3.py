with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

nums = lines[0][2:].replace('[', '').replace(']', '')
nums = list(map(int, nums.split(',')))
A = nums

last_coord = [A[0] + 1000, A[1] + 1000]

n = 0
for x in range(A[0], last_coord[0] + 1):
    for y in range(A[1], last_coord[1] + 1):
        rx, ry = 0, 0
        for _ in range(100):
            # Multiply
            nx = rx * rx - ry * ry
            ny = rx * ry + ry * rx
            # Divide
            rx, ry = int(nx / 100000) + x, int(ny / 100000) + y
            if abs(rx) > 1000000 or abs(ry) > 1000000:
                break
        else:  
            n += 1


print(n)
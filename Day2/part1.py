with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

nums = lines[0][2:].replace('[', '').replace(']', '')
nums = list(map(int, nums.split(',')))
A = nums

def add(z1, z2):
    return [z1[0] + z2[0], z1[1] + z2[1]]

def multiply(z1, z2):
    return [z1[0]*z2[0] - z1[1]*z2[1],
            z1[0]*z2[1] + z1[1]*z2[0]]

def divide(z1, z2):
    return [z1[0] // z2[0], z1[1] // z2[1]]
  

res = [0,0]
for _ in range(3):
  res = multiply(res, res)
  res = divide(res, [10,10])

  res = add(res, A)
print(res)

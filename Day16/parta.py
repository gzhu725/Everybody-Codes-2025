spell = [1, 2, 4, 8, 36, 55, 78, 81, 99, 117, 139, 142, 167, 190, 209, 228, 231, 251, 275, 296, 303, 326, 344, 357, 385, 461, 601, 733, 887, 953]
total_blocks = 202520252025000

def blocks_needed(L):
    return sum(L // n for n in spell)

low, high = 0, total_blocks
while low < high:
    mid = (low + high + 1) // 2
    if blocks_needed(mid) <= total_blocks:
        low = mid
    else:
        high = mid - 1

print("Max wall length:", low)

with open("input.txt") as f:
    pattern = f.readline().strip()

n = len(pattern)

total_len = n * 1000

mentors_base = {'A': [], 'B': [], 'C': []}
novices_base = {'a': [], 'b': [], 'c': []}

for i in range(len(pattern)):
    if pattern[i] in mentors_base:
        mentors_base[pattern[i]].append(i)
    elif pattern[i] in novices_base:
        novices_base[pattern[i]].append(i)

mentors = {}
novices = {}

for k, v in mentors_base.items():
    if v:
        mentors[k.lower()] = [b + k * n for k in range(1000) for b in v]

for k, v in novices_base.items():
    if v:
        novices[k] = [b + k * n for k in range(1000) for b in v]

# all positions to check ^ 


total_pairs = 0
for low in ("a", "b", "c"):
    if low not in mentors or low not in novices:
        continue

    m = mentors[low]
    n_list = novices[low]
    mi_left = mi_right = 0
    m_len = len(m)

    for pos in n_list:
        L = pos - 1000
        R = pos + 1000

        while mi_left < m_len and m[mi_left] < L:
            mi_left += 1

        while mi_right < m_len and m[mi_right] <= R:
            mi_right += 1

        total_pairs += (mi_right - mi_left)

print(total_pairs)

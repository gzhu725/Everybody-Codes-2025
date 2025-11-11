with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

parts = lines[0].split(':')
bones = list(map(int, parts[1].split(",")))

centers = []
res = [[-1, -1, -1] for _ in range(len(bones))]
p = 0

for b in bones:
    flag = False
    for i in range(p, len(res)):
        if res[i][1] == -1:
            res[i][1] = b
            flag = True
        elif res[i][0] == -1 and b < res[i][1]:
            res[i][0] = b
            flag = True
        elif res[i][2] == -1 and b > res[i][1]:
            res[i][2] = b
            flag = True
        
        if flag:
            break
    
    if res[p][0] != -1 and res[p][1] != -1 and res[p][2] != -1:
        p += 1

s = ""
for r in res:
    if r[1] != -1:
        s += str(r[1])

centers.append(int(s))



print(centers[0])
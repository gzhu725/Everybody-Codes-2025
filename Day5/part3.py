with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

swords = []

for line in lines:
    parts = line.split(':')
    sword_id = int(parts[0])
    bones = list(map(int, parts[1].split(',')))
    
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

    quality = int(''.join(str(r[1]) for r in res if r[1] != -1))
    
    levels = []
    for r in res:
        if r[1] != -1:
            level_str = ''
            if r[0] != -1:
                level_str += str(r[0])
            level_str += str(r[1])
            if r[2] != -1:
                level_str += str(r[2])
            levels.append(int(level_str))
    
    swords.append((sword_id, quality, levels))

swords.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)

checksum = sum((i + 1) * sword[0] for i, sword in enumerate(swords))
print(checksum)
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

initial_columns = list(map(int, lines))


def flock_checksum(columns):
    s = 0
    for i in range(len(columns)):
        s += (i*1) * columns[i]

def phase1_step(columns):
    moved = False
    new_columns = columns[:]
    for i in range(len(columns) - 1):
        if new_columns[i] > new_columns[i+1]:
            new_columns[i] -= 1
            new_columns[i+1] += 1
            moved = True
    return new_columns, moved

def phase2_step(columns):
    moved = False
    new_columns = columns[:]
    for i in range(len(columns) - 1):
        if new_columns[i] < new_columns[i+1]:
            new_columns[i] += 1
            new_columns[i+1] -= 1
            moved = True
    return new_columns, moved

def simulate_ducks(columns, total_rounds):
    columns = columns[:]
    phase = 1
    checksums = [flock_checksum(columns)]
    
    round_num = 0
    while len(set(columns)) != 1:
        if phase == 1:
            columns, moved = phase1_step(columns)
            if not moved:
                phase = 2
        else:
            columns, moved = phase2_step(columns)
        round_num += 1
        checksums.append(flock_checksum(columns))
        print(round_num)

    return round_num, columns


total_rounds = 11
final_columns, checksums = simulate_ducks(initial_columns, total_rounds)

print(final_columns - 1)
def total_rounds_to_balance(columns):

    n = len(columns)
    total_ducks = sum(columns)
    target = total_ducks // n  # final ducks per column

    phase1_max = 0
    excess = 0
    for i in range(n-1):
        diff = columns[i] - columns[i+1]
        if diff > 0:
            excess += diff
            phase1_max = max(phase1_max, excess)
        else:
            excess = 0  # reset if no forward move

   
    cols = columns[:]
    moved = True
    while moved:
        moved = False
        for i in range(n-1):
            if cols[i] > cols[i+1]:
                cols[i] -= 1
                cols[i+1] += 1
                moved = True

    phase2_max = 0
    cum = 0
    for c in cols:
        cum += c - target
        phase2_max = max(phase2_max, abs(cum))

    total_rounds = phase1_max + phase2_max
    return total_rounds


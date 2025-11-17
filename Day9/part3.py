with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

seqs = {}
for line in lines:
    idx, dna = line.split(':')
    seqs[int(idx)] = dna

def is_child(child, p1, p2):
    """Return (is_valid_child, matches_with_p1, matches_with_p2)"""
    m1 = m2 = 0
    for a, b, c in zip(p1, p2, child):
        # Child must match *one* parent at each position
        if c != a and c != b:
            return (False, 0, 0)
        if c == a:
            m1 += 1
        if c == b:
            m2 += 1
    return (True, m1, m2)

def find_families(seqs):
    """Return list of (child, parent1, parent2, m1, m2, product)."""
    ids = sorted(seqs.keys())
    n = len(ids)
    results = []

    for i in range(n):
        for j in range(i+1, n):
            p1 = ids[i]
            p2 = ids[j]
            dna1 = seqs[p1]
            dna2 = seqs[p2]

            for k in ids:
                if k in (p1, p2):
                    continue
                child_dna = seqs[k]

                valid, m1, m2 = is_child(child_dna, dna1, dna2)
                if valid:
                    results.append((k, p1, p2, m1, m2, m1*m2))

    return results

from collections import defaultdict, deque

def build_family_graph(families):
    graph = defaultdict(set)
    nodes = set()

    # Build graph edges
    for child, p1, p2, *_ in families:
        nodes.update([child, p1, p2])
        graph[p1].add(child)
        graph[child].add(p1)
        graph[p2].add(child)
        graph[child].add(p2)

    # BFS to get connected components
    visited = set()
    components = []

    for node in nodes:
        if node not in visited:
            q = deque([node])
            visited.add(node)
            comp = set([node])

            while q:
                cur = q.popleft()
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        comp.add(neighbor)
                        q.append(neighbor)

            components.append(comp)

    return components


families = find_families(seqs)
res = build_family_graph(families)

largest_fam = max(res, key=len)
print(sum(largest_fam))
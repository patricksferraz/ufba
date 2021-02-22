Nodes = {}
Graph = {}
candidates = []
path = []

def best(candidates):
    def f(candidate):
        ef = Nodes[candidate[0]]
        p_cost = candidate[1]
        return p_cost + ef
    return min(candidates, key=f)

N = int(input().rstrip())
for node in range(1, N+1):
    ef = int(input().rstrip())
    Nodes[str(node)] = ef

rel = int(input().rstrip())
for _ in range(rel):
    entry = input().rstrip()
    a, b, cost = entry.split(' ')
    if Graph.get(a, None) is None:
        Graph[a] = []
    Graph[a].append({'n': b, 'cost': int(cost)})

entry = input().rstrip()
start, objective = entry.split(' ')

candidates.append((start, 0))
while candidates:
    current, p_cost = best(candidates)
    candidates.remove((current,p_cost))
    path.append(current)
    if current == objective:
        break
    if Graph.get(current, None) is not None:
        for neighbor in Graph[current]:
            candidates.append((neighbor['n'], neighbor['cost'] + p_cost))

print("-".join(path))

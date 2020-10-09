Graph = {}
stack = []
path = []

entry = input().rstrip()
nodes, rel = entry.split(' ')

for _ in range(int(rel)):
    entry = input().rstrip()
    a, b = entry.split(' ')
    if Graph.get(a, None) is None:
        Graph[a] = []
    Graph[a].append(b)

entry = input().rstrip()
start, objective = entry.split(' ')

stack.append(start)
while stack:
    current = stack[-1]
    if Graph.get(current):
        nxt = Graph[current].pop(0)
        stack.append(nxt)
    else:
        visited = stack.pop()
        path.append(visited)
        if visited == objective:
            break

print("-".join(path))

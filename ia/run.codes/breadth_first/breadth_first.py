Graph = {}
queue = []
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

queue.append(start)
while queue:
    current = queue.pop(0)
    path.append(current)
    if current == objective:
        break
    if Graph.get(current):
        for neighbor in Graph.get(current):
            queue.append(neighbor)

print("-".join(path))

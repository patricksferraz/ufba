Graph = {}
stack = []
path = []
visited = {}

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
path.append(start)
while stack:
    current = stack[-1]
    visited[current] = True
    if current == objective:
        break
    if Graph.get(current):
        nxt = Graph[current].pop(0)
        if visited.get(nxt):
            break
        path.append(nxt)
        stack.append(nxt)
    else:
        stack.pop()

print("-".join(path))

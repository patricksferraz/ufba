#!/usr/bin/env python3

Graph = {}
Nodes = {}
stack = []
queue = []

def best(candidates, objective):
    def f(candidate):
        if candidate['n'] == objective:
            return 0
        ef = Nodes[candidate['n']]
        cost = candidate['cost']
        return cost + ef
    return min(candidates, key=f)

def drop(node):
    global Graph
    Nodes.pop(node)
    Graph = {n:filter(lambda rel: rel['n'] != node, Graph[n]) for n in Graph}

entry = input().rstrip()
nodes, rel = entry.split(' ')

for _ in range(int(rel)):
    entry = input().rstrip()
    a, b = entry.split(' ')
    if Graph.get(a, None) is None:
        Graph[a] = []
    Graph[a].append(b)

nodes = int(input())

for _ in range(nodes):
    entry = input().rstrip()
    node, value = entry.split(' ')
    Nodes[node] = int(value)

queue.append(('1', 0))
while queue:
    current, lv = queue.pop(0)
    if Graph.get(current, None):
        for neighbor in Graph[current]:
            if Nodes.get(neighbor, None) is None:
                queue.append((neighbor, lv+1))
        stack.append((current, lv))

func = {
    0: max,
    1: min,
}
while stack:
    current, lv = stack.pop()
    values = [Nodes[n] for n in Graph[current]]
    Nodes[current] = func[lv%2](values)


print(Nodes['1'])

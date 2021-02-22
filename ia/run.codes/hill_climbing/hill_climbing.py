#!/usr/bin/env python2

Nodes = {}
Graph = {}
state = []
path = []

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

N = int(raw_input())
for node in range(1, N+1):
    ef = int(raw_input())
    Nodes[str(node)] = ef

rel = int(raw_input())
for _ in range(rel):
    entry = raw_input()
    a, b, cost = entry.split(' ')
    if Graph.get(a, None) is None:
        Graph[a] = []
    Graph[a].append({'n': b, 'cost': int(cost)})

entry = raw_input()
start, objective = entry.split(' ')

state.append((start, 0))
while state:
    current, p_cost = state.pop(0)
    path.append(current)
    if current == objective:
        break
    if not Graph.get(current, None):
        drop(current)
        path = []
        state.append((start, 0))
    else:
        nxt = best(Graph[current], objective)
        state.append((nxt['n'], p_cost+nxt['cost']))

print("-".join(path))

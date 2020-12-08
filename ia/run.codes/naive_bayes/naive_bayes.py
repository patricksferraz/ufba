#!/usr/bin/env python3

base = {}
clss = {}

entry = input().rstrip()
rows, cols = entry.split(' ')

for row in range(int(rows)):
    entry = input().rstrip()
    instance = entry.split(' ')
    cls = instance.pop(-1)

    clss[cls] = clss.get(cls, 0) + 1
    if cls not in base:
        base[cls] = {}

    for col in range(len(instance)):
        if col not in base[cls]:
            base[cls][col] = []
        base[cls][col].append(instance[col])

entry = input().rstrip()
test = entry.split(' ')

prob = {}
for cls in clss:
    cls_prob = clss[cls] / int(rows)

    if cls not in prob:
        prob[cls] = 1

    for col, value in enumerate(test):
        func = base[cls][col].count(value) / len(base[cls][col])
        prob[cls] *= func #if func > 0 else 1

    prob[cls] *= cls_prob

print(max(prob, key=prob.get))

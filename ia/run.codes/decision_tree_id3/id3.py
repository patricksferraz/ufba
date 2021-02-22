#!/usr/bin/env python3

import math

base = {}


def filter_base(S: dict, attr: int, value: int):
    return dict((k, v) for k, v in S.items() if v[attr] == value)


def get_dist(S: dict, cls_col: int, **kwargs):
    """kwargs: attr: int, value: int"""
    if 'attr' in kwargs:
        attr = kwargs.get('attr')
        value = kwargs.get('value')
        S = filter_base(S=S, attr=attr, value=value)

    positive = [v[cls_col] for v in S.values()].count(1)
    negative = [v[cls_col] for v in S.values()].count(0)
    return {'+': positive, '-': negative}


def entropy(dist: dict):
    total = sum(dist.values())
    res = 0
    try:
        for count in dist.values():
            prob = count / total
            res -= prob * math.log2(prob)
    finally:
        return res


def gain(S: dict, attr: int, cls_col: int, total: int):
    """"""
    res = entropy(get_dist(S=S, cls_col=cls_col))

    for value in [0, 1]:
        dist = get_dist(S=S, cls_col=cls_col, attr=attr, value=value)
        prob = sum(dist.values()) / total
        res -= prob * entropy(dist)

    return res


def best_gain(S: dict, attrs: list, cls_col: int):
    gains = {}
    for attr in attrs:
        gains[attr] = gain(S=S, attr=attr, cls_col=cls_col, total=len(S))
    best = max(gains, key=gains.get)
    return best


entry = input().rstrip()
rows, cols = [int(v) for v in entry.split(' ')]
cls_col = cols - 1
attrs = list(range(cls_col))

for row in range(rows):
    entry = input().rstrip()
    instance = [int(v) for v in entry.split(' ')]

    if row not in base:
        base[row] = {}

    for col in range(cols):
        base[row][col] = instance[col]

entry = input().rstrip()
test = [int(v) for v in entry.split(' ')]

queue = []
tree = {}

root = best_gain(S=base, attrs=attrs, cls_col=cls_col)
queue.append((root, base))
while queue:
    # print(f'q {[v for v,c in queue]}')
    # print(f'attrs {attrs}')
    current, base = queue.pop(0)
    # print(f'c {current}')

    if current not in tree:
        tree[current] = {}
        attrs.remove(current)
        for value in [0, 1]:
            cbase = filter_base(S=base, attr=current, value=value)
            cdist = get_dist(
                S=cbase, cls_col=cls_col, attr=current, value=value
            )

            if entropy(dist=cdist) == 0:
                tree[current][value] = max(cdist, key=cdist.get)
            else:
                # TODO: removes this pog
                try:
                    tree[current][value] = best_gain(
                        S=cbase, attrs=attrs, cls_col=cls_col
                    )
                    queue.append((tree[current][value], cbase))
                except:
                    tree[current][value] = '-'
    # print(tree)


current = root
while current != '+' and current != '-':
    current = tree[current][test[current]]

print(1 if current == '+' else 0)

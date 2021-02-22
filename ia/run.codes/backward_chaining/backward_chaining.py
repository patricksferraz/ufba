#!/usr/bin/env python3

import re

stack = []
kl_base = {}


def norm(string: str) -> str:
    string = string.replace('^', 'and')
    string = string.replace('!', 'not')
    string = string.replace('|', 'or')
    return string


entry = input().rstrip()
while entry != 'END':
    rule, key = entry.split(' => ')
    kl_base[key] = {
        'rule': norm(rule),
        'attr': [x for x in re.split(r'\W', rule) if x != ''],
    }
    entry = input().rstrip()

facts = input().rstrip().split(',')
for fact in facts:
    kl_base[fact] = {'rule': True, 'attr': []}

query = input().rstrip()
stack.append(query)

while query not in facts:
    current = stack[-1]

    if current in facts:
        stack.pop(-1)
        continue

    if current in kl_base:

        for attr in kl_base[current]['attr']:
            if attr in facts:
                kl_base[current]['attr'].remove(attr)
                globals()[attr] = kl_base[attr]['rule']
            else:
                stack.append(attr)

        if not kl_base[current]['attr']:
            kl_base[current]['rule'] = eval(kl_base[current]['rule'])
            globals()[current] = kl_base[current]['rule']
            facts.append(current)
            stack.pop(-1)

    else:
        kl_base[current] = {'rule': False, 'attr': []}
        globals()[current] = kl_base[current]['rule']
        facts.append(current)
        stack.pop(-1)

print('TRUE' if kl_base[query]['rule'] else 'FALSE')

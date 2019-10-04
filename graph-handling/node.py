import json


class Node:
    def __init__(self, node: str, neighbor: list):
        self.name: str = node
        self.neighbor: list = neighbor
        self.degree: int = len(neighbor)

    def __str__(self):
        return json.dumps(
            {
                "node": {
                    "name": self.name,
                    "neighbor": self.neighbor,
                    "degree": self.degree,
                }
            }
        )

    def __lt__(self, other):
        return self.degree < other.degree

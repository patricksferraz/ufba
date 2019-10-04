from node import Node
import json


class Graph:
    def __init__(self, graph: dict = None):
        self.graph: dict = graph
        self.nodes: list[Node] = Graph.init_nodes(graph)

    def __str__(self):
        return json.dumps(self.graph)

    def add_node(self, node: Node) -> None:
        (self.nodes).append(node)

    def exists_adj(self, node: Node, adj_matrix: dict) -> None:
        try:
            for n in self.nodes:
                if node.name in adj_matrix[n.name]:
                    return True
            return False
        except KeyError:
            return False

    @staticmethod
    def adj_matrix(nodes: list) -> dict:
        """Returns the adjacency matrix

        Arguments:
            nodes {list} -- List with nodes

        Returns:
            dict -- adjacency matrix
        """
        adj_matrix = {}
        try:
            for n in nodes:
                adj_matrix[n.name] = {}
                for c in n.neighbor:
                    if c in adj_matrix[n.name]:
                        adj_matrix[n.name][c] += 1
                    else:
                        adj_matrix[n.name][c] = 1
        except Exception as e:
            print(f"[INFO] {e}")
        finally:
            return adj_matrix

    @staticmethod
    def init_nodes(graph: dict) -> list:
        """Initializes the graph nodes, adds name, neighbor and degree

        Arguments:
            graph {dict} -- graph

        Returns:
            list -- list with nodes
        """
        nodes = []
        try:
            for n in graph.keys():
                nodes.append(Node(n, graph[n]))
        except AttributeError:
            return nodes
        finally:
            return nodes

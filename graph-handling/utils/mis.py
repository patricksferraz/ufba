from graph import Graph
import random


def mis(graph: Graph) -> Graph:
    """Returns the maximum independent set in a graph

    Arguments:
        graph {Graph} -- input graph

    Returns:
        Graph -- graph with maximum independent set
    """
    # init graph for maximum independet set
    mis = Graph()
    # shuffles nodes before ordering by degree
    nodes = graph.nodes
    random.shuffle(nodes)
    nodes.sort()

    for n in nodes:
        if not mis.exists_adj(n, Graph.adj_matrix(mis.nodes)):
            mis.add_node(n)

    return mis

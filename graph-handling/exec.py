from graph import Graph
from utils.mis import mis
import argparse
import json

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--graph", required=True, help="file with graph")
args = vars(ap.parse_args())

struct = json.loads(open(args["graph"], "r").read())

graph = Graph(struct)
graph_mis = mis(graph)

for n in graph_mis.nodes:
    print(n)

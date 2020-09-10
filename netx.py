import csv
import networkx as nx
from networkx import connected_components
from networkx.algorithms.community import asyn_fluidc

if __name__ == '__main__':
    G = nx.Graph()
    with open('similarities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t Adding {row[0]} and {row[1]} .')
                G.add_edge(row[0], row[1])
                line_count += 1
        print(f'Processed {line_count} lines.')
        print(f'Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.')
    S = [G.subgraph(c).copy() for c in connected_components(G)]
    for subgraph in S:
        nodes = subgraph.number_of_nodes()
        if nodes > 5:
            communities = asyn_fluidc(subgraph, round(nodes/50), 1000)
            for community in communities:
                print(community)
        else:
            print(subgraph.nodes)

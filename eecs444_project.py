import networkx as nx
import random


def main():
    # Watts Strogatz Ring Graph
    # do it at various levels
    #
    ring_lattice = nx.watts_strogatz_graph(16, 4, 0)
    simple_contagion(ring_lattice)


# simple contagion propogation
def simple_contagion(in_graph):
    print('in')
    infected_nodes = set()

    # pick the starting node.
    infected_nodes.add(0)
    # add the ego network of that node.
    infected_nodes = infected_nodes.union(set(in_graph.neighbors(0)))

    time_step_number = 0
    while len(infected_nodes) < in_graph.number_of_nodes():
        nodes_to_add = set()
        for node in infected_nodes:
            to_infect_node = random.choices(list(in_graph.neighbors(node)))[0]
            nodes_to_add.add(to_infect_node)

        print(nodes_to_add)
        infected_nodes = infected_nodes.union(nodes_to_add)
        print(time_step_number, ":", infected_nodes)
        time_step_number += 1

        # while there are nodes being added to the graph, continue looping
        # For each infected node, pick a neighbor of that node and infect it (even if it is already infected)
        # print out the state of infected nodes.


if __name__ == '__main__':
    main()

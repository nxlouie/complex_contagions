import networkx as nx
import random


def main():
    # Watts Strogatz Ring Graph
    # do it at various levels
    #
    ring_lattice = nx.watts_strogatz_graph(16, 4, 0)
    simple_contagion(ring_lattice)
    complex_contagion(ring_lattice, 2)


# simple contagion propagation
def simple_contagion(in_graph):
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


def complex_contagion(in_graph, a):
    """

    :param in_graph: networkx graph object to run the complex contagion on
    :param a: number of activated nodes required for activation
    :return:
    """
    in_graph = nx.watts_strogatz_graph(16, 4, 0)

    infected_nodes = set()
    # pick the starting node.
    infected_nodes.add(0)
    # add the ego network of that node.
    infected_nodes = infected_nodes.union(set(in_graph.neighbors(0)))

    time_step_number = 0

    # TODO: not a good end condition for complex
    while len(infected_nodes) < in_graph.number_of_nodes():
        nodes_to_add = set()
        for node in infected_nodes:
            to_infect_node = random.choices(list(in_graph.neighbors(node)))[0]

            # Check this node has enough critical mass to infect
            if len(infected_nodes.intersection(set(in_graph.neighbors(to_infect_node)))) >= a:
                nodes_to_add.add(to_infect_node)

        print(nodes_to_add)
        infected_nodes = infected_nodes.union(nodes_to_add)
        print(time_step_number, ":", infected_nodes)
        time_step_number += 1


if __name__ == '__main__':
    main()

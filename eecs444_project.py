import networkx as nx
import random
import matplotlib.pyplot as plt


def main():
    # Watts Strogatz Ring Graph
    # do it at various levels
    ring_lattice = nx.watts_strogatz_graph(16, 4, 0)
    # nx.draw(ring_lattice)
    # plt.draw()
    # plt.show()
    simple_contagion(ring_lattice)
    complex_contagion(ring_lattice, 2)

    # 2 dimensional lattice with Moore neighborhoods
    moore_lattice = create_moore_lattice(6, 8, 2)
    # nx.draw(moore_lattice)
    # plt.draw()
    # plt.show()


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


def create_moore_lattice(m, n, radius=1):

    moore_lattice = nx.generators.lattice.grid_2d_graph(m, n)

    for node in moore_lattice.nodes():
        nodes_to_add = set()
        print("NODE", node)
        for row in range(node[0] - radius, node[0] + radius + 1):
            for column in range(node[1] - radius, node[1] + radius + 1):
                if row < 0 or row > m - 1 or column < 0 or column > n - 1:
                    continue
                print(row, column)
                nodes_to_add.add((row, column))
        for add_node in nodes_to_add:
            if node != add_node:
                moore_lattice.add_edge(node, add_node)

    return moore_lattice


if __name__ == '__main__':
    main()

import networkx as nx
import random
import matplotlib.pyplot as plt


def main():
    # Watts Strogatz Ring Graph
    # do it at various levels
    ring_lattice = nx.watts_strogatz_graph(100, 4, 0)
    # nx.draw(ring_lattice)
    # plt.draw()
    # plt.show()
    print("Ring simple ", simple_contagion(ring_lattice, 0))
    print("Ring complex", complex_contagion(ring_lattice, 0, 2))

    # 2 dimensional lattice with Moore neighborhoods
    #moore_lattice = create_moore_lattice(100, 100, 0.000001, 1)
    # nx.draw(moore_lattice)
    # plt.draw()
    # plt.show()
    # print("Moore simple ", simple_contagion(moore_lattice, (0, 0)))
    # print("Moore complex", complex_contagion(moore_lattice, (0, 0), 2))

    generate_plot()


# simple contagion propagation
def simple_contagion(in_graph, start_node):
    infected_nodes = set()
    # pick the starting node.
    infected_nodes.add(start_node)
    # add the ego network of that node.
    infected_nodes = infected_nodes.union(set(in_graph.neighbors(start_node)))

    time_step_number = 0
    while len(infected_nodes) < in_graph.number_of_nodes():
        nodes_to_add = set()
        for node in infected_nodes:
            to_infect_node = random.choices(list(in_graph.neighbors(node)))[0]
            nodes_to_add.add(to_infect_node)

        # print(nodes_to_add)
        infected_nodes = infected_nodes.union(nodes_to_add)
        # print(time_step_number, ":", infected_nodes)
        time_step_number += 1

        # while there are nodes being added to the graph, continue looping
        # For each infected node, pick a neighbor of that node and infect it (even if it is already infected)
        # print out the state of infected nodes.

    return time_step_number


def complex_contagion(in_graph, start_node, a):
    """

    :param in_graph: networkx graph object to run the complex contagion on
    :param a: number of activated nodes required for activation
    :return:
    """

    infected_nodes = set()
    # pick the starting node.
    infected_nodes.add(start_node)
    # add the ego network of that node.
    infected_nodes = infected_nodes.union(set(in_graph.neighbors(start_node)))

    time_step_number = 0

    # TODO: not a good end condition for complex
    while len(infected_nodes) < in_graph.number_of_nodes() * 0.99 and time_step_number <= 500000:
        nodes_to_add = set()
        for node in infected_nodes:
            to_infect_node = random.choices(list(in_graph.neighbors(node)))[0]

            # Check this node has enough critical mass to infect
            if len(infected_nodes.intersection(set(in_graph.neighbors(to_infect_node)))) >= a:
                nodes_to_add.add(to_infect_node)

            time_step_number += 1

            if len(infected_nodes) >= in_graph.number_of_nodes() * 0.99 or time_step_number > 500000:
                break

        # print(nodes_to_add)
        infected_nodes = infected_nodes.union(nodes_to_add)
        # print(time_step_number, ":", infected_nodes)

    return time_step_number


def generate_plot():
    # print("Moore simple ", simple_contagion(moore_lattice, (0, 0)))
    # print("Moore complex", complex_contagion(moore_lattice, (0, 0), 2))
    #for i in [-6, -4, -3, -2, -1, -0.9, -0.8, -0.7, -0.69, -0.68, -0.67, -0.66, -0.65, -0.64, -0.63, -0.62]:
    for i in [-6, -4, -3, -2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.39, -1.38, -1.37, -1.36, -1.35, -1.34, -1.33, -1.32, -1.31, -1.3, -1.2, -1.1, -1]:
        moore_lattice = create_moore_lattice(50, 50, 10**i, 1)
        print("Complex", i, complex_contagion(moore_lattice, (25, 25), 3))


def create_moore_lattice(m, n, p, radius=1):

    moore_lattice = nx.generators.lattice.grid_2d_graph(m, n)

    for node in moore_lattice.nodes():
        nodes_to_add = set()
        for row in range(node[0] - radius, node[0] + radius + 1):
            for column in range(node[1] - radius, node[1] + radius + 1):
                if row < 0 or row > m - 1 or column < 0 or column > n - 1:
                    continue
                nodes_to_add.add((row, column))
        for add_node in nodes_to_add:
            if node != add_node:
                moore_lattice.add_edge(node, add_node)

    for node in moore_lattice.nodes():
        neighbors = list(moore_lattice.neighbors(node))
        edges_to_be_deleted = []
        for neighbor in neighbors:
            delete_edge = random.choices([True, False], [p, 1 - p])[0]
            if delete_edge:
                edges_to_be_deleted.append((node, neighbor))

        unconnected = set(n for n in moore_lattice.nodes() if n not in neighbors)
        for i in range(len(edges_to_be_deleted)):
            dest = random.sample(unconnected, 1)[0]
            unconnected.remove(dest)
            moore_lattice.add_edge(node, dest)

        for edge in edges_to_be_deleted:
            moore_lattice.remove_edge(edge[0], edge[1])

    return moore_lattice


if __name__ == '__main__':
    main()

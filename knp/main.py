import math
import random
import networkx as ax
import matplotlib.pyplot as plt
import networkx as nx


def init_matrix(nodes_count):
    matrix = [[0 for x in range(nodes_count)] for x in range(nodes_count)]
    for i in range(nodes_count):
        for n in range(i, nodes_count):
            if n != i:
                weight = random.randint(0, 20)
                matrix[i][n] = weight
                matrix[n][i] = weight
    return matrix


def make_graph(matrix):
    graph = nx.Graph()
    for i in range(len(matrix)):
        graph.add_node(i)

    for i in range(len(matrix)):
        for n in range(i, len(matrix[i])):
            if matrix[i][n] != 0:
                graph.add_edge(i, n, weight=matrix[i][n])
    return graph


def draw(graph):
    position = nx.spring_layout(graph, k=5)
    nx.draw(graph, with_labels=True, pos=position, font_weight='regular')
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, position, edge_labels=labels)
    plt.show()


def min_tree(matrix):
    nodes = [node for node in range(len(matrix))]

    minimal_dist = math.inf
    edges = []
    edge = (0, 0, 0)
    for k in range(len(matrix)):
        for n in range(k, len(matrix[k])):
            if matrix[k][n] < minimal_dist and matrix[k][n] != 0:
                minimal_dist = matrix[k][n]
                edge = (k, n, matrix[k][n])

    edges.append(edge)
    nodes.remove(edge[0])
    nodes.remove(edge[1])

    while len(nodes) > 0:
        minimal_dist = math.inf

        for k in range(len(matrix)):
            if k in nodes:
                continue
            for n in range(len(matrix[k])):
                if matrix[k][n] < minimal_dist and matrix[k][n] != 0 and n in nodes:
                    minimal_dist = matrix[k][n]
                    edge = (k, n, matrix[k][n])

        edges.append(edge)
        nodes.remove(edge[1])

    new_matrix = [[0 for x in range(len(matrix))] for x in range(len(matrix))]

    for ed in edges:
        new_matrix[ed[0]][ed[1]] = ed[2]
        new_matrix[ed[1]][ed[0]] = ed[2]

    return new_matrix


def cluster_matrix(matrix, clusters_count):
    matrix_n = []
    for l in matrix:
        matrix_n.append(l.copy())
    for m in range(clusters_count - 1):
        maximum_edge = (0, 0, 0)
        for k in range(len(matrix_n)):
            for n in range(k, len(matrix_n)):
                if matrix_n[k][n] > maximum_edge[2]:
                    maximum_edge = (k, n, matrix_n[k][n])

        matrix_n[maximum_edge[0]][maximum_edge[1]] = 0
        matrix_n[maximum_edge[1]][maximum_edge[0]] = 0

    return matrix_n


matrix = init_matrix(8)
graph = make_graph(matrix)
draw(graph)
ostovtree_matrix = min_tree(matrix)
ostovtree_graph = make_graph(ostovtree_matrix)
draw(ostovtree_graph)
clustermatrix = cluster_matrix(ostovtree_matrix, 5)
clustergraph = make_graph(clustermatrix)
draw(clustergraph)
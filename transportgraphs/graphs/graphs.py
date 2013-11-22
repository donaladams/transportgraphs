"""
graphs.py

A simple graph library in python
"""

import heapq

PATH_COST = "d"
PREDECESSOR = "p"

class Node(object):
    """ Represents a node in a graph """

    def __init__(self, node_id):
        self.node_id = node_id
        self.workspace = {}

    def get_node_id(self):
        """ returns the node_id """
        return self.node_id

    def set_value(self, key, value):
        """ Sets a value in the node's workspace """
        self.workspace[key] = value

    def get_value(self, key):
        """ Returns a value from the nodes workspace if
            it exists, otherwise returns none (default
            behaviour of dict.get(key))"""
        return self.workspace.get(key)

    def __str__(self):
        return "Node {0}, {1}".format(self.node_id, self.workspace)

    def __lt__(self, other):
        """ Custom implementation of less-than method. Based on the current lowest
        cost of the path in the graph to this node. """
        self_has = self.workspace.has_key(PATH_COST)
        if not self_has:
            return False

        other_has = other.workspace.has_key(PATH_COST)
        if not other_has:
            return False

        return self.workspace[PATH_COST] < other.workspace[PATH_COST]


class Edge(object):
    """ Represents an edge in a graph """

    def __init__(self, first, second, weight=0):
        self.first = first
        self.second = second
        self.weight = weight

    def get_first_vertex(self):
        """ Retrieves the first vertex in the edge """
        return self.first

    def get_second_vertex(self):
        """ Retrieves the second vertex in the edge """
        return self.second

    def __str__(self):
        return "Edge ({0}, {1}, {2})".format(
            self.get_first_vertex(), self.get_second_vertex(), self.weight)


def create_path_from_graph(graph, start, end):
    """ given a graph, start and end vertex, this creates a path object
        implied by that graph """
    cost = graph.get_vertex_value(end, PATH_COST)
    reverse_path = []

    current = end
    while current != start:
        reverse_path.append(current)
        current = graph.get_vertex_value(current, PREDECESSOR)
    reverse_path.append(start)

    reverse_path.reverse()
    path = tuple(reverse_path)
    return Path(path, cost)


class Path(object):
    """ represents a path through a graph with an associated cost """
    def __init__(self, path, cost):
        self.path = tuple(path)
        self.cost = cost

    def __len__(self):
        return len(self.path)

    def __getitem__(self, i):
        return self.path[i]

    def __str__(self):
        return "cost: {0} path: {1}".format(self.cost, self.path)

class WeightedDiGraph(object):
    """ Class representing a weighted directed graph """

    def __init__(self, n_vertices, edge_list):
        self.vertex_count = n_vertices
        self.vertices = {i:Node(i) for i in range(n_vertices)}
        self.graph = {
            key: {
                edge[1]:
                    Edge(
                        edge[0],
                        edge[1],
                        edge[2])
                    for edge in edge_list if edge[0] == key
                }
                for key in xrange(n_vertices)
            }

    def get_vertices(self):
        """ return list of vertices in graph """
        return self.vertices.values()

    def get_vertices_dict(self):
        """ return a dictionary mapping vertex ids to vertices """
        return self.vertices

    def get_edges(self):
        """ gets a list of all edges in graph """
        return [self.graph[u][v]
                    for u in self.graph.keys()
                        for v in self.graph[u].keys()]

    def get_neighbours(self, node_id):
        """ returns list of vertices reachable in one hop from the
            node with id node_id in the graph """
        return [self.vertices[i] for i in self.graph[node_id].keys()]

    def get_parents(self, node_id):
        """ Gets the parents of a node. O(Edges) operation"""
        return [self.vertices[i] for i in set([
            edge.get_first_vertex() for edge in self.get_edges()
                if edge.get_second_vertex() == node_id
                ]
            )]

    def set_vertex_value(self, vertex_id, key, value):
        """ sets a value on the given vertex at the given key """
        self.vertices[vertex_id].set_value(key,value)

    def get_vertex_value(self, vertex_id, key):
        """ gets a value on the given vertex at the given key """
        return self.vertices[vertex_id].get_value(key)

    def get_weight_of_edge(self, first, second):
        """ returns the weight of a given edge in the graph """
        if self.graph[first].has_key(second):
            return self.graph[first][second].weight
        return float("+inf")

    def print_edges(self):
        """ prints edges of the graph to the console """
        for u_id in self.graph.keys():
            for v_id in self.graph[u_id].keys():
                print u_id, v_id, str(self.graph[u_id][v_id])

    def print_vertices(self):
        """ print vertices in graph to the console  """
        for vertex in self.get_vertices():
            print vertex

    def has_negative_edge_weights(self):
        """ Indicates if the graph contains negative edge weights. """
        return any(map(lambda edge: edge.weight < 0, self.get_edges()))

def init_single_source(graph, source_id):
    """ initialises a graph for single source shortest path problems """
    for vertex in graph.get_vertices():
        if source_id == vertex.node_id:
            graph.set_vertex_value(vertex.node_id, PATH_COST, 0)
        else:
            graph.set_vertex_value(vertex.node_id, PATH_COST, float("+inf"))
            graph.set_vertex_value(vertex.node_id, PREDECESSOR, None)

def relax(graph, u_vertex, v_vertex):
    """ performs the relaxation update if necessary for a vertex """
    u_id = u_vertex.node_id
    v_id = v_vertex.node_id

    u_distance = graph.get_vertex_value(u_id, PATH_COST)
    v_distance = graph.get_vertex_value(v_id, PATH_COST)

    new_distance = u_distance + graph.get_weight_of_edge(u_id, v_id)

    if v_distance > new_distance:
        graph.set_vertex_value(v_id, PATH_COST, new_distance)
        graph.set_vertex_value(v_id, PREDECESSOR, u_id)

def make_heap(graph):
    """ makes a heap out of the vertices of a graph, ordered by """
    q_vertices = graph.get_vertices()

    heap = []
    for elem in q_vertices:
        heapq.heappush(heap, elem)

    return heap

def dijikstra(graph, source):
    """ Performs the dijikstra alrgorithm for the single-source
        shortest path on the given_graph from the given source """

    if graph.has_negative_edge_weights():
        raise ValueError(
            "Dijikstra's algorithm cannot be run on graphs \\\
             with negative edge weights")

    init_single_source(graph, source)
    s_vertices = []
    heap = make_heap(graph)

    while len(heap) > 0:
        min_vertex = heapq.heappop(heap)
        s_vertices.append(min_vertex)
        neighbours = graph.get_neighbours(min_vertex.get_node_id())

        for vertex in neighbours:
            relax(graph, min_vertex, vertex)

        heapq.heapify(heap)

def bellman_ford(graph, source):
    """ Performs the bellman-ford alrgorithm for the single-source
        shortest path on the given_graph from the given source """
    init_single_source(graph, source)

    edges = graph.get_edges()
    vertices = graph.get_vertices_dict()

    for i in xrange(graph.vertex_count):
        for edge in edges:
            relax(
                graph,
                vertices[edge.get_first_vertex()],
                vertices[edge.get_second_vertex()])

    for edge in edges:
        v_id = edge.get_second_vertex()
        u_id = edge.get_first_vertex()
        v_distance = graph.get_vertex_value(v_id, PATH_COST)
        u_distance = graph.get_vertex_value(u_id, PATH_COST)
        weight = graph.get_weight_of_edge(u_id, v_id)
        if v_distance > u_distance + weight:
            return False

    return True

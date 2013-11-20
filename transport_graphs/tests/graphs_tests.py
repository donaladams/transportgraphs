import nose
from graphs import WeightedDiGraph
from graphs import bellman_ford
from graphs import create_path_from_graph
from graphs import Path
from graphs import dijikstra

class TestWeightedDigraph(object):

    def test_construction(self):
        """ It builds a correct graph """
        number_vertices = 5
        edges = [
            (0, 1, 5),
            (1, 4, 7),
            (3, 2, 8),
            (2, 4, 5),
            (1, 3, 9),
            (2, 1, 1),
            (1, 2, 1)
            ]

        graph = WeightedDiGraph(number_vertices, edges)

        # number of vertices is correct
        assert graph.vertex_count == number_vertices
        # vertices dict has correct keys
        assert set(graph.vertices.keys()) == set(range(number_vertices))
        # get_vertices returns the correct number of vertices
        assert len(graph.get_vertices()) == number_vertices
        # all node workspaces are empty
        assert all(map(lambda x: not x.workspace, graph.get_vertices()))
        # number of edges is correct
        assert len(graph.get_edges()) == len(edges)
        # edge weights are correct
        edge_tuples = [
            (
                edge.get_first_vertex(),
                edge.get_second_vertex(),
                edge.weight
                )
            for edge in graph.get_edges()]

        assert set(edges) == set(edge_tuples)


    def test_get_neighbours(self):
        """ It gets neighbours correctly """
        number_vertices = 6
        edges = [
            (0, 1, 5),
            (1, 4, 7),
            (3, 2, 8),
            (2, 4, 5),
            (1, 3, 9),
            (2, 1, 1),
            (1, 2, 1)
            ]

        graph = WeightedDiGraph(number_vertices, edges)
        vertices = graph.get_vertices_dict()

        # no neighbours
        assert set(graph.get_neighbours(5)) == set([])
        # one neighbour
        assert set(graph.get_neighbours(0)) == set([vertices[1]])
        # many neighbours
        assert set(graph.get_neighbours(1)) == set(
            [
                vertices[2],
                vertices[3],
                vertices[4],
                ]
            )

    def test_get_parents(self):
        """ It gets parents correctly """
        number_vertices = 6
        edges = [
            (0, 1, 5),
            (1, 4, 7),
            (3, 2, 8),
            (2, 4, 5),
            (1, 3, 9),
            (2, 1, 1),
            (1, 2, 1),
            (4, 5, 3)
            ]

        graph = WeightedDiGraph(number_vertices, edges)
        vertices = graph.get_vertices_dict()

        # no parents
        assert set(graph.get_parents(0)) == set([])
        # one parent
        assert set(graph.get_parents(5)) == set([vertices[4]])
        # many parents
        assert set(graph.get_parents(1)) == set(
            [
                vertices[0],
                vertices[2]
                ]
            )

class TestPath(object):
    """ Unit tests for path object """

    def test_str(self):
        """ Makes sure the __str__ function returns the correct format """
        path = Path([0,1,2,3,4], 10)
        assert str(path) == "cost: 10 path: (0, 1, 2, 3, 4)"

class TestBellmanFord(object):

    def test_shortest_paths(self):
        """ Shortest paths found in graph """
        edges = [
            (0, 1, 5),
            (1, 4, 7),
            (3, 2, 8),
            (2, 4, 5),
            (1, 3, 9),
            (2, 1, 1),
            (1, 2, 1)
            ]

        graph = WeightedDiGraph(5, edges)
        root = 0

        bellman_ford(graph, root)

        assert str(create_path_from_graph(graph, root, 0)) == "cost: 0 path: (0,)"
        assert str(create_path_from_graph(graph, root, 1)) == "cost: 5 path: (0, 1)"
        assert str(create_path_from_graph(graph, root, 2)) == "cost: 6 path: (0, 1, 2)"
        assert str(create_path_from_graph(graph, root, 3)) == "cost: 14 path: (0, 1, 3)"
        assert str(create_path_from_graph(graph, root, 4)) == "cost: 11 path: (0, 1, 2, 4)"

class TestDijikstra(object):

    def test_shortest_paths(self):
        """ Shortest paths found in graph """
        edges = [
            (0, 1, 5),
            (1, 4, 7),
            (3, 2, 8),
            (2, 4, 5),
            (1, 3, 9),
            (2, 1, 1),
            (1, 2, 1)
            ]

        graph = WeightedDiGraph(5, edges)
        root = 0

        dijikstra(graph, root)

        assert str(create_path_from_graph(graph, root, 0)) == "cost: 0 path: (0,)"
        assert str(create_path_from_graph(graph, root, 1)) == "cost: 5 path: (0, 1)"
        assert str(create_path_from_graph(graph, root, 2)) == "cost: 6 path: (0, 1, 2)"
        assert str(create_path_from_graph(graph, root, 3)) == "cost: 14 path: (0, 1, 3)"
        assert str(create_path_from_graph(graph, root, 4)) == "cost: 11 path: (0, 1, 2, 4)"







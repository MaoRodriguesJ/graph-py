import unittest
from graph import Graph

class GraphTestCase(unittest.TestCase):
    def setUp(self):
        dictionary = {"x1":set(["x2","x3","x8"]),
                      "x2":set(["x1"]),
                      "x3":set(["x1"]),
                      "x4":set(["x8"]), 
                      "x5":set(["x6","x7","x8"]),
                      "x6":set(["x5"]),
                      "x7":set(["x5"]),
                      "x8":set(["x1","x4","x5"])}
        self.g = Graph(dictionary)

    def test_order(self):
        self.assertEqual(8, self.g.get_order())

    def test_degree(self):
        self.g.connect("x5", "x4")
        self.assertEqual(4, self.g.get_degree("x5"))
        self.g.disconnect("x5", "x4")
        self.assertEqual(3, self.g.get_degree("x5"))

    def test_connected(self):
        self.g.add_vertex("x9")
        self.assertFalse(self.g.is_connected())
        self.g.remove_vertex("x9")
        self.assertTrue(self.g.is_connected())

    def test_adjacents(self):
        adjacents = {"x6", "x7", "x8"}
        self.assertEqual(adjacents, self.g.get_adjacents("x5"))
        self.g.connect("x5", "x4")
        self.assertFalse(adjacents == self.g.get_adjacents("x5"))
        self.g.disconnect("x5", "x4")

    def test_tree(self):
        self.g.add_vertex("x9")
        self.assertFalse(self.g.is_tree())
        self.g.connect("x5", "x9")
        self.assertTrue(self.g.is_tree())
        self.g.remove_vertex("x9")

    def test_transitive_closure(self):
        transitive_closure = {"x2", "x1", "x4", "x8", "x7", "x6", "x5", "x3"}
        self.assertEqual(transitive_closure, self.g.get_transitive_closure("x5"))
        self.g.add_vertex("x9")
        self.g.connect("x5", "x9")
        self.assertFalse(transitive_closure == self.g.get_transitive_closure("x5"))

    def test_depth_search(self):
        visited = self.g.dict.keys()
        print("Depth Search Test:\n")
        self.assertEqual(visited, self.g.depth_first_search("x8"))

    def test_is_complete(self):
        for keys in self.g.dict.keys():
            [self.g.connect(keys, vertex) for vertex in self.g.dict.keys()]
        self.assertTrue(self.g.is_complete())
        self.assertTrue(self.g.is_regular())


if __name__ == '__main__': 
    unittest.main()
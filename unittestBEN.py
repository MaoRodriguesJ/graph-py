import unittest
from graph import Graph

class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def test_add_vertex(self):
        for i in range(1, 7):
            self.g.add_vertex(i)
        
        vertexes = [1, 2, 3, 4, 5, 6] 
        self.assertEqual(vertexes, list(self.g.dict.keys()))

    def test_remove_vertex(self):
        for i in range(1,7):
            self.g.add_vertex(i)
        self.g.remove_vertex(1)
        vertexes = [2, 3, 4, 5, 6]
        self.assertEqual(vertexes, list(self.g.dict.keys()))

    def test_connect(self):
        self.g.add_vertex(1)
        self.g.add_vertex(2)
        self.g.connect(1,2)
        adjacents = {2}
        self.assertEqual(adjacents, self.g.dict[1])
        adjacents = {1}
        self.assertEqual(adjacents, self.g.dict[2])

    def test_disconnect(self):
        self.g.add_vertex(1)
        self.g.add_vertex(2)
        self.g.connect(1,2)
        self.g.disconnect(1,2)
        adjacents = set()
        self.assertEqual(adjacents, self.g.dict[1])
        self.assertEqual(adjacents, self.g.dict[2])

    def test_order(self):
        for i in range (1,100):
            self.g.add_vertex(i)
        self.assertEqual(99, self.g.get_order())

    def test_vertixes(self):
        for i in range (1,5):
                        self.g.add_vertex(i)
        vertexes = [1, 2, 3, 4]
        self.assertEqual(vertexes, list(self.g.dict.keys()))
        
    def test_get_random_vertex(self):
        for i in range (1,5):
            self.g.add_vertex(i)
        self.assertTrue(self.g.get_random_vertex() == 1 or 2 or 3 or 4)
    
    def test_adjacents(self):
        for i in range (1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(1,4)
        adjacents = {2, 3, 4}
        self.assertEqual(adjacents, self.g.get_adjacents(1))
    
    def test_degree(self):
        for i in range (1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(1,4)
        degree = 3
        self.assertEqual(degree, self.g.get_degree(1))
        degree = 1
        self.assertEqual(degree, self.g.get_degree(2))
        self.assertEqual(degree, self.g.get_degree(3)) 
        

    def test_is_regular(self):
        for i in range(1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(2,3)
        self.g.connect(1,4)
        self.g.connect(2,4)
        self.g.connect(3,4)
        self.assertTrue(self.g.is_regular())
        self.g.disconnect(3,4)
        self.assertFalse(self.g.is_regular())

    def test_is_complete(self):
        for i in range(1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(2,3)
        self.g.connect(1,4)
        self.g.connect(2,4)
        self.g.connect(3,4)
        self.assertTrue(self.g.is_complete())
        self.g.disconnect(3,4)
        self.assertFalse(self.g.is_complete())

    def test_transitive_closure(self):
        for i in range(1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(2,3)
        self.g.connect(1,4)
        self.g.connect(2,4)
        self.g.connect(3,4)
        transitive = {1,2,3,4} 
        self.assertEqual(transitive, self.g.get_transitive_closure(1))
        self.g.add_vertex(5)
        self.assertEqual(transitive, self.g.get_transitive_closure(1))

    def test_is_connected(self):
        for i in range(1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(2,3)
        self.g.connect(1,4)
        self.g.connect(2,4)
        self.g.connect(3,4)
        self.assertTrue(self.g.is_connected())
        self.g.add_vertex(5)
        self.assertFalse(self.g.is_connected())


    def test_is_tree(self):
        for i in range(1,5):
            self.g.add_vertex(i)
        self.g.connect(1,2)
        self.g.connect(1,3)
        self.g.connect(2,3)
        self.g.connect(1,4)
        self.g.connect(2,4)
        self.g.connect(3,4)
        self.assertFalse(self.g.is_tree())
        self.g.disconnect(2,4)
        self.g.disconnect(3,4)
        self.g.disconnect(2,3)
        self.assertTrue(self.g.is_tree())

if __name__ == '__main__': 
    unittest.main()
from graph import Graph

dictionary = {"x1":set(["x2","x3","x8"]),
			  "x2":set(["x1"]),
			  "x3":set(["x1"]),
			  "x4":set(["x8"]), 
			  "x5":set(["x6","x7","x8"]),
			  "x6":set(["x5"]),
			  "x7":set(["x5"]),
			  "x8":set(["x1","x4","x5"])}

g = Graph(dictionary)

print ("Ordem do grafo =", g.get_order())

g.connect("x5", "x4")
print ("Grau vértice x5 após conectar ao x4 =", g.get_degree("x5"))

g.disconnect("x5","x4")
print ("Grau vértice x5 após desconectar do x4 =", g.get_degree("x5"))

print("Grafo Regular =",g.is_regular())

g.add_vertex("x9")
print("Grafo Conexo (após adição de x9) =", g.is_connected())

g.remove_vertex("x9")
print("Grafo Conexo (após remoção de x9)=", g.is_connected())

print("Grafo Completo =", g.is_complete())

print("Vértices do grafo =", g.get_vertexes())

print("Vértice aleatório do grafo =", g.get_random_vertex())

print("Vértices adjacentes a x5 =", g.get_adjacents("x5"))

print("Fecho transitivo do vertice x5 =", g.get_transitive_closure("x5"))
g.add_vertex("x9")
print("Fecho transitivo do vertice x5 (após adicionar x9)=",
	  g.get_transitive_closure("x5"))
print("Grafo Árvore =", g.is_tree())

g.connect("x5", "x9")
print("Fecho transitivo do vertice x5 (após conectar a x9)=",
	  g.get_transitive_closure("x5"))

print("Grafo Árvore =", g.is_tree())

g.remove_vertex("x9")

print("Fecho transitivo do vertice x5 (após remover x9)=",
	  g.get_transitive_closure("x5"))

print("Busca em profundidade:")
g.depth_first_search("x8")

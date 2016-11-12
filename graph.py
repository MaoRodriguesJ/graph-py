import random


class Graph(object):

    def __init__ (self, dict={}):
        """ Inicializa os vértices do grafo """
        self.dict = dict

    def add_vertex(self, vertex):
        """ Adiciona o vértice "vertex" no grafo, caso ele não exista """
        if vertex not in self.dict:
            self.dict[vertex] = set()

    def remove_vertex(self, vertex):
        """ Remove o vértice "vertex" do grafo, e as conexões que o envolvam """
        if vertex in self.dict:
            del self.dict[vertex]
            for vertexes in self.dict:
                if vertex in self.dict[vertexes]:
                    self.dict[vertexes].remove(vertex)

    def connect(self, v1, v2):
        """ Conecta dois vértices do grafo """
        if v1 in self.dict and v2 in self.dict:
            self.dict[v1].add(v2)
            self.dict[v2].add(v1)

    def disconnect(self, v1, v2):
        """ Desconecta dois vértices do grafo """
        if v1 in self.dict and v2 in self.dict:
            self.dict[v1].discard(v2)
            self.dict[v2].discard(v1)

    def get_order(self):
        """ Informa a ordem do grafo """
        return len(self.dict)

    def get_vertexes(self):
        """ Informa todos vértices do grafo """
        return self.dict.keys()

    def get_random_vertex(self):
        """ Informa um vértice aleatório do grafo """
        return random.choice(list(self.dict.keys()))

    def get_adjacents(self, vertex):
        """ Informa os vértices adjacentes ao vértice "vertex" """
        if vertex in self.dict:
            return self.dict[vertex]
          
    def get_degree(self, vertex):
        """ Informa o grau do vértice "vertex" """
        if vertex in self.dict:
            return len(self.dict[vertex])

    def is_regular(self):
        """ Verifica se todos vértices do grafo possuem mesmo grau """
        base_degree = self.get_degree(list(self.dict.keys())[0])
        return not any(self.get_degree(vertex) != base_degree
                       for vertex in self.dict)

    def is_complete(self):
        """ Verifica se o grafo é completo """
        for vertexes in self.dict:
            if (self.dict[vertexes].union([vertex])) != set(self.dict.keys()):
                return False
        return True

    def get_transitive_closure(self, vertex, transitive_clousure=set()):
        """ Retorna o fecho transitivo de um determinado vértice "vertex" """
        transitive_clousure.add(vertex)

        for vertexes in self.get_adjacents(vertex):
            if vertexes not in transitive_clousure:
                transitive_clousure = self.get_transitive_closure(vertexes, transitive_clousure)

        return transitive_clousure
    
    def is_connected(self):
        """ Verifica se o grafo é conexo """
        set_aux = self.get_transitive_closure(self.get_random_vertex())
        if set_aux == set(self.dict.keys()):
            return True
        return False

    def is_tree(self):
        """ Verifica se o grafo é uma árvore """
        v = self.get_random_vertex()
        return self.is_connected() and not(self.detect_cycle(v, v))

    def detect_cycle(v, v_before, visited=set()):
        """ Verifica se o vértice "v" faz parte de algum ciclo """
        if v in visited:
            return True
        visited.add(v)
        for v_adj in self.get_adjacents(v):
            if v_adj != v_before:
                if detect_cycle(v_adj, v, visited):
                    return True
        visited.discard(v)
        return False
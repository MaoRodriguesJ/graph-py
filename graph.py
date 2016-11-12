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
      for vertexes in self.dict
        if vertex in self.dict[vertexes]
          self.dict[vertexes].remove(vertex)

  def connect(self, v1, v2):
    """ Conecta dois vértices do grafo """
    if v1 in self.dict and v2 in self.dict
      self.dict[v1].add(v2)
      self.dict[v2].add(v1)

  def disconnect(self, v1, v2):
    """ Desconecta dois vértices do grafo """
    if v1 in self.dict and v2 in self.dict
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
    if vertex in self.dict
      return self.dict[vertex]
          
  def get_degree(self, vertex):
    """ Informa o grau do vértice "vertex" """
    if vertex in self.dict
      return len(self.dict[vertex])

  def is_regular(self):
  def is_complete(self):
  def get_transitive_closure(self, vertex):
  def is_connected(self):
  def is_tree(self):
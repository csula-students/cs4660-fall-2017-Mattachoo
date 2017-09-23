""" 
graph module defines the knowledge representations fil
A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """ 
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    f = open(file_path)
    
    for newNode in range(int(f.readline())):
        graph.add_node(Node(newNode))
    for line in f:
        temp = line.split(":")
        graph.add_edge(Edge(Node(int(temp[0])),Node(int(temp[1])),temp[2]))
    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one o:f the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        for edge in self.adjacency_list[node_1]:
            if edge.to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        return [neigh.to_node for neigh in self.adjacency_list[node]]

    def add_node(self, node):

        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list.update({node: []})
            return True

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for nodes in self.adjacency_list:
                self.adjacency_list[nodes] = [edge for edge in self.adjacency_list[nodes] if edge.to_node != node]

            return True
        else:
            return False
    def add_edge(self, edge):
        if edge.from_node in self.adjacency_list and edge.to_node in self.adjacency_list:
            if edge in self.adjacency_list[edge.from_node]:
                return False
            else:
                self.adjacency_list[edge.from_node].append(edge)
                return True
        else:
            return False
    def remove_edge(self, edge):
        if(edge.from_node in self.adjacency_list):
            if edge in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge)
                return True
            else:
                return False
        return False
class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix =[]
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodesa
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            if self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)] is not 0:
                return True
            else:
                return False
        else: 
            return False

    def neighbors(self, node):
        if node in self.nodes:
            neighbors = []
            index = 0
            for neigh in self.adjacency_matrix[self.__get_node_index(node)]:
                if neigh is not 0:
                    neighbors.append(self.nodes[index])
                index += 1
            return neighbors
        else:
            return []
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.adjacency_matrix.append([0])
            for row in self.adjacency_matrix:
                row.append(0)
                self.adjacency_matrix[self.__get_node_index(node)].append(0)
            return True
        else:
            return False

    def remove_node(self, node):
        if node in self.nodes:
            del self.adjacency_matrix[self.__get_node_index(node)]
            for spot in self.adjacency_matrix:
                del spot[self.__get_node_index(node)]
            self.nodes.remove(node)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            if self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] ==0:
                self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] =edge.weight
                return True
            else:
                return False
        else:
            return False
    def remove_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            if self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] !=0:
                self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] =0
                return True
            else:
                return False
        else:
            return False
    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
            else:
                return False

    def neighbors(self, node):
        neighbor = []
        for edge in self.edges:
            if edge.from_node == node:
                neighbor.append(edge.to_node)
        return neighbor

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
        #    for edge in self.edges:
         #       if edge.from_node is node:
          #          self.edges.remove(edge)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False

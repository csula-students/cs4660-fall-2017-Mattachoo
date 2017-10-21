"""
< package is for some quick utility methods
such as parsing
"""
from . import graph as gr
class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)                                                        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)
def parse_grid_file(graph, file_path):
        """
        ParseGridFile parses the grid file implementation from the file path line
        by line and construct the nodes & edges to be added to graph
        Returns graph object
        """
        x = 0
        y = 0
        f = open(file_path)
        print(file_path)
        grid = []
        for line in f:
            if line[0] is not '+':
                grid.append([line[i:i+2].rstrip("\n") for i in range(1, len(line)-2, 2)])
        f.close()
                #grid.append(line)
               # for character in line:
                #    if character is not '#' and character is not '|':
                 #       graph.add_node(gr.Node(Tile(x,y, character)))
                    
                  #  x+=1
            #x = 0
            #y +=1
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] is not '##':
                    graph.add_node(gr.Node(Tile(x,y, grid[y][x])))
                    if x-1 >= 0:
                        if  grid[y][x-1] is not '##':
                            graph.add_edge(gr.Edge(gr.Node(Tile(x,y, grid[y][x])), gr.Node(Tile(x-1,y, grid[y][x-1])), 1))
                            graph.add_edge(gr.Edge(gr.Node(Tile(x-1,y, grid[y][x-1])), gr.Node(Tile(x,y, grid[y][x])), 1))
                    if(y -1 >= 0):
                        if grid[y-1][x] is not '##':
                            graph.add_edge(gr.Edge(gr.Node(Tile(x,y, grid[y][x])), gr.Node(Tile(x,y-1, grid[y-1][x])), 1))
                            graph.add_edge(gr.Edge(gr.Node(Tile(x,y-1, grid[y-1][x])), gr.Node(Tile(x,y, grid[y][x])), 1))
        print("returning")
        # TODO: read the filepath line by line to construct nodes & edges
        # TODO: for each node/edge above, add it to graph
        return graph
def convert_edge_to_grid_actions(edges):

        """
         
        Convert a list of edges to a string of actions in the grid base tile
    
        e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    
        """
        actions = []
        for edge in edges:
            if(edge.from_node.x > edge.to_node.x):
                actions.append('W')
            if(edge.from_node.x < edge.to_node.x):
                actions.append('E')
            if(edge.from_node.y > edge.to_node.y):    
                actions.append('N')
            if(edge.from_node.x < edge.to_node.x):
                actions.append('S')


        return str(actions)


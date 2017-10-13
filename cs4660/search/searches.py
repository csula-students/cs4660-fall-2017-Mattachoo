"""
Searches module defines all different search algorithms
"""
from graph import graph as gr
def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    
def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    parents = {}
    dfs_help(graph, initial_node, parents,{})
    actions = []
    curr = dest_node
    while curr != initial_node:
        actions = [gr.Edge(parents[curr], curr, graph.distance(parents[curr], curr))] + actions
        curr = parents[curr]
    return actions 
    
def dfs_help(graph, curr,  parents, discovered):
    for node in graph.neighbors(curr):
        if node in discovered:
            continue
        discovered[node] = True
        parents[node] = curr
        dfs_help(graph,node,parents,discovered)

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

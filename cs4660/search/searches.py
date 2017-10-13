"""
Searches module defines all different search algorithms
"""
from graph import graph as gr
from queue import *
def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    nodes = []
    parents = {}
    actions = []
    end_tile = ((None, None, None))
    q = Queue()
    q.put((initial_node, 0, None))
    while(q.qsize() > 0):
        u = q.get()
        for node in graph.neighbors(u[0]):
            if node not in nodes:
                if node == dest_node:
                    end_tile = u
                nodes.append(node)
                q.put((node, graph.distance(u[2], node), u))
    while (end_tile[2] is not None):
        actions.append(gr.Edge(end_tile[2][0], end_tile[0], graph.distance(end_tile[2][0], end_tile[0])))
        end_tile = end_tile[2]
    actions.reverse()
   # print("\n" + str(actions))
    #actions.append(gr.Edge(actions[len(actions)-1].to_node, dest_node, graph.distance(actions[len(actions)-1].to_node, dest_node)))
    print("\n" + str(actions))
    return actions
def bfs_help(graph, start, parents):
    #for node in graph:
    pass

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

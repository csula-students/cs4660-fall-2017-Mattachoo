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
    actions = []
    end_tile = ((None,  None))
    q = Queue()
    q.put((initial_node, None))
    while(q.qsize() > 0):
        u = q.get()
        for node in graph.neighbors(u[0]):
            if node not in nodes:
                if node == dest_node:
                    end_tile = u
                nodes.append(node)
                q.put((node, u))
    while (end_tile[1] is not None):
        actions.append(gr.Edge(end_tile[1][0], end_tile[0], graph.distance(end_tile[1][0], end_tile[0])))
        end_tile = end_tile[1]
    actions.reverse()
    actions.append(gr.Edge(actions[len(actions)-1].to_node, dest_node, graph.distance(actions[len(actions)-1].to_node, dest_node)))
    return actions

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
    parents = {}
    dist = {}
    dist[initial_node] = 0
    parents[initial_node] = None
    actions = []
    q = PriorityQueue()
    q.put((0, initial_node))
    v = None
    for v in graph.neighbors(initial_node):
        if v is not initial_node:
            dist[v] = float('inf')
            parents[v] = None
        q.put((dist[v], v))
    while(q.qsize() > 0):
        u = q.get()
        for node in graph.neighbors(u[1]):
            if node not in dist:
                dist[node] = 10000000
            alt = u[0] + graph.distance(u[1],node)
            if alt < dist[node]:
                dist[node] = alt
                parents[node] = u[1]
                q.put((alt, node))
    #            actions.append(gr.Edge(u[1], node, graph.distance(u[1], node)))
    node = dest_node
    while (parents[node] is not None):
        actions.append(gr.Edge(parents[node], node, graph.distance(parents[node], node)))
        node = parents[node]
    actions.reverse()
    #actions.append(gr.Edge(actions[len(actions)-1].to_node, dest_node, graph.distance(actions[len(actions)-1].to_node, dest_node)))
    return actions

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

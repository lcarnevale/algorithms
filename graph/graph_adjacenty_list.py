# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2022, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = 'Algorithms and Data Structure, University of Messina'
__description__ = 'Graph - Adjacency List'


def create_graph():
    return dict()


def add_node(graph, node):
    if not node in graph:
        graph[node] = []
    return graph

def add_nodes(graph, nodes):
    """ Add multiple nodes.

    Args:
        graph (dict): graph data structure
        nodes (list): list of nodes
    
    Returns:
        (dict) graph data structure updated
    """
    for node in nodes:
        graph = add_node(graph, node)
    return graph

def get_nodes(graph):
    return list(graph.keys())

def nodes_count(graph):
    return len(graph)

def remove_vertex(graph, v):
    if v in graph:
        for node in graph[v]:
            if v in graph[node]:
                graph[node].remove(v)
        del graph[v]
    return graph


def add_edge(graph, u, v):
    if u in graph and v in graph:
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
    return graph

def add_edges(graph, edges):
    for edge in edges:
        graph = add_edge(graph, *edge)
    return graph

def get_edge(graph, edge):
    u, v = edge
    if u in graph[v] and v in graph[u]:
        return True
    else:
        return False

def get_edges(graph):
    edges = []
    for k, v in graph.items():
        for u in v:
            if (k,u) not in edges and (u,k) not in edges:
                edges.append((k,u))
    return edges

def edges_count(graph):
    return len(get_edges(graph))

def incident_edges(graph, u):
    edges = []
    if u in graph:
        for node in graph[u]:
            edges.append((u, node))
    return edges

def remove_edge(graph, edge):
    u, v = edge
    if u not in graph or v not in graph:
        print("Almeno uno dei nodi non esiste")
    else:
        if u in graph[v]:
            graph[v].remove(u)
        if v in graph[u]:
            graph[u].remove(v)
    return graph


def degree(graph):
    deg = dict()
    for node in graph:
        deg[node] = len(graph[node])
    return deg

def is_complete(graph):
    n = len(graph)
    for node in graph:
        if len(graph[node]) < n - 1:
            return False
    return True

def dfs_recursive(graph, start, explored=[]):
    if start not in explored:
        explored.append(start)
        print("\n%s not explored yet. Explored[]: %s" % (start, explored))
        print("\nGet list of vertex reachable from %s" % (start))
        for v in list(graph[start]):
            print("v=%s, explored[]: %s" % (v, explored))
            if v not in explored:
                print("Explore it!")
                explored.append(v)
                print("Explored[]: %s, and traverse %s recursivelly" % (explored, v))
                dfs_recursive(graph, v, explored)
    return explored

def dfs_iterative(graph, start):
    explored = []
    stack = []
    stack.append(start)
    while stack:
        u = stack.pop()
        if u not in explored:
            explored.append(u)
            for v in list(graph[u]):
                stack.append(v)
    return explored

def dfs(graph):
    """ Traverse in DFS

    -1: white
    0: gray
    1: black
    """
    exploration = dict()
    for u in get_nodes(graph):
        exploration[u] = -1 # white
    print("Exploration[]: %s" % (exploration))

    for u in exploration.keys():
        print("Exploration[u] = %s is -1 (white)?" % (exploration[u]))
        if exploration[u] == -1:
            dfs_visit(graph, u, exploration)
    return exploration

def dfs_visit(graph, vertex, exploration):
    exploration[vertex] = 0
    print("Exploration[u] = %s is 0 (gray), Exploration[]: %s" % (exploration[vertex], exploration))
    for v in graph[vertex]:
        print("Exploration[u] = %s is -1 (white)? Exploration[]: %s" % (exploration[v], exploration))
        if exploration[v] == -1:
            dfs_visit(graph, v, exploration)
    exploration[vertex] = 1
    print("Exploration[u] = %s is 1 (black), Exploration[]: %s" % (exploration[vertex], exploration))

def bfs(graph, s):
    exploration = dict()
    for u in get_nodes(graph):
        if u != s:
            exploration[u] = -1
    print("Exploration[]: %s" % (exploration))

    exploration[s] = 0
    stack = list()
    stack.append(s)
    print("Stacking %s, Q[]: %s" % (s, stack))
    print("Exploration[]: %s" % (exploration))

    while stack:
        u = stack.pop()
        print("Exploring vertex adjacent to %s (u)" % (u))
        for v in graph[u]:
            print("Exploration[v] = %s is -1 (white)? Exploration[]: %s" % (exploration[v], exploration))
            if exploration[v] == -1:
                exploration[v] = 0
                stack.append(v)
                print("Stacking %s, Q[]: %s" % (v, stack))
                print("Exploration[]: %s" % (exploration))
        exploration[u] = 1
        print("Exploration[u] = %s is 1 (black), Exploration[]: %s" % (exploration[u], exploration))
    return exploration

def main():
    graph = create_graph()
    
    add_nodes(graph, ['SFO','ORD','BOS','JFK','DFW','LAX','MIA'])
    print( "Nodes[]: %s " % (get_nodes(graph)) )
    print( "Nodes size: %s" % (nodes_count(graph)) )

    add_edges(graph, [ 
        ['BOS','SFO'],
        ['BOS','JFK'],
        ['BOS','MIA'],
        ['JFK','SFO'],
        ['JFK','BOS'],
        ['JFK','DFW'],
        ['JFK','MIA'],
        ['ORD','DFW'],
        ['ORD','MIA'],
        ['DFW','ORD'],
        ['DFW','SFO'],
        ['DFW','LAX'],
        ['MIA','DFW'],
        ['MIA','LAX'],
    ])
    print( "Edges[]: %s " % (get_edges(graph)) )
    print( "Edges size: %s" % (edges_count(graph)) )

    node = 'BOS'
    print( "Edges incidents to %s: %s" % (node, incident_edges(graph, node)))

    print( "Graph degree: %s" % (degree(graph)) )
    print( "Graph is complete: %s" % (is_complete(graph)) )

    print( "Graph[]: %s" % (graph) )
    print( "Traverse from %s: %s" % (node, dfs_recursive(graph, node)) )
    print( "Traverse from %s: %s" % (node, dfs_iterative(graph, node)) )

    print(dfs(graph))

    print(bfs(graph, node))



if __name__ == "__main__":
    main()
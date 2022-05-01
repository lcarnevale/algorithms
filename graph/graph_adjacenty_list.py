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
        ['DFW','LXA'],
        ['MIA','DFW'],
        ['MIA','LXA'],
    ])
    print( "Edges[]: %s " % (get_edges(graph)) )
    print( "Edges size: %s" % (edges_count(graph)) )

    node = 'BOS'
    print( "Edges incidents to %s: %s" % (node, incident_edges(graph, node)))

    print( "Graph degree: %s" % (degree(graph)) )
    print( "Graph is complete: %s" % (is_complete(graph)) )


if __name__ == "__main__":
    main()
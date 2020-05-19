import sys
import numpy as np 

class Node():
    def __init__(self, name, index, h, graph):
        self.node_name = name 
        self.node_index = index
        self.h = h 
        self.g = 9999
        self.f = self.g + self.h      
        self.graph = graph
        self.previous_node = None

A = Node('A', 0, 16, {'B':5, 'C':5})
B = Node('B', 1, 17, {'A':5, "C":4, 'D':3})
C = Node('C', 2, 13, {'A':5, 'B':4, 'D':7, 'E':7, 'H':8})
D = Node('D', 3, 16, {'B':3, 'C':7, 'H':11, 'K':16, 'L':13, 'M':14})
E = Node('E', 4, 16, {'C':7, 'H':5, 'F':4})
F = Node('F', 5, 20, {'E':4, 'G':9})
G = Node('G', 6, 12, {'F':9, 'N':12})
H = Node('H', 7, 11, {'C':8, 'D':11, 'E':5, 'I':3})
I = Node('I', 8, 10, {'H':3, 'J':4})
J = Node('J', 9, 8, {'I':4, 'N':3, 'P':8})
K = Node('K', 10, 4, {'D':16, 'L':5, 'N':7, 'P':4})
L = Node('L', 11, 7, {'D':13, 'K':5, 'M':9, 'O':4})
M = Node('M', 12, 10, {'D':14, 'L':9, 'O':5})
N = Node('N', 13, 7, {'G':12, 'J':3, 'K':7, 'P':7 })
O = Node('O', 14, 5, {'L':4, 'M':5})
P = Node('p', 15, 0, {'J':8, 'K':4, 'N':7})

nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]
current_node = 'A'
open_nodes = ['A']
closed_nodes = []

A.g = 0
A.f = A.g + A.h 
def A_star_step():
    global A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P
    global current_node, open_nodes, closed_nodes

    for node in list(globals()[current_node].graph.keys()):
        # N = globals()[node]
        if node not in open_nodes and node not in closed_nodes :
            open_nodes.append(node) 
        if node not in closed_nodes:
            if globals()[node].previous_node == None and not A:
                globals()[node].previous_node = current_node
                globals()[node].g = globals()[current_node].g + globals()[node].graph[current_node]
                globals()[node].f = globals()[node].g + globals()[node].h
            elif globals()[node].f > globals()[current_node].g + globals()[node].graph[current_node] + globals()[node].h:
                globals()[node].previous_node = current_node
                globals()[node].g = globals()[current_node].g + globals()[node].graph[current_node]
                globals()[node].f = globals()[node].g + globals()[node].h


    closed_nodes.append(open_nodes.pop(open_nodes.index(current_node)))
    acitve_f = []
    for node in open_nodes:
        acitve_f.append( globals()[node].f)
    i = acitve_f.index(min(acitve_f))
    current_node = open_nodes[i]

for i in range(3):   
    A_star_step()
    print(current_node)
    print(open_nodes)
    print(closed_nodes)
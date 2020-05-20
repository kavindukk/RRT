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

A = Node('A', 0, 16, {'1':5, '2':5}) # 0
B = Node('B', 1, 17, {'0':5, "2":4, '3':3}) # 1
C = Node('C', 2, 13, {'0':5, '1':4, '3':7, '4':7, '7':8}) # 2
D = Node('D', 3, 16, {'1':3, '2':7, '7':11, '10':16, '11':13, '12':14}) # 3 
E = Node('E', 4, 16, {'2':7, '7':5, '5':4}) #4
F = Node('F', 5, 20, {'4':4, '6':9}) #5
G = Node('G', 6, 12, {'5':9, '13':12}) #6
H = Node('H', 7, 11, {'2':8, '3':11, '4':5, '8':3}) #7
I = Node('I', 8, 10, {'7':3, '9':4}) #8
J = Node('J', 9, 8,  {'8':4, '13':3, '15':8}) #9
K = Node('K', 10, 4, {'3':16,'11':5, '13':7, '15':4}) #10
L = Node('L', 11, 7, {'3':13,'10':5, '12':9, '14':4}) #11
M = Node('M', 12, 10,{'3':14,'11':9, '14':5}) #12
N = Node('N', 13, 7, {'6':12,'9':3, '10':7, '15':7 }) #13
O = Node('O', 14, 5, {'11':4,'12':5}) #14
P = Node('p', 15, 0, {'9':8, '10':4, '13':7}) #15

nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]
current_node = 'A'
open_nodes = ['A']
closed_nodes = []

class A_star():
    def __init__(self, nodes, start_index, end_index):
        self.nodes = nodes
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = str(start_index)
        self.open_nodes = [str(start_index)]
        self.closed_nodes = []
        self.nodes[start_index].g = 0
        self.nodes[start_index].f = self.nodes[start_index].g + self.nodes[start_index].h
    def A_star_step(self):   
        connected_nodes = list(self.nodes[int(self.current_index)].graph.keys()) 
        for node in connected_nodes:
            # N = globals()[node]
            if node not in self.open_nodes and node not in self.closed_nodes :
                self.open_nodes.append(node) 
            if node not in self.closed_nodes:                
                if self.nodes[int(node)].previous_node == None and not self.nodes[self.start_index]:
                    self.nodes[int(node)].previous_node = self.current_index
                    self.nodes[int(self.current_index)].g
                    self.nodes[int(node)].g = self.nodes[int(self.current_index)].g + self.nodes[int(node)].graph[self.current_index]
                    self.nodes[int(node)].f = self.nodes[int(node)].g + self.nodes[int(node)].h
                elif self.nodes[int(node)].f > self.nodes[int(self.current_index)].g + self.nodes[int(node)].graph[self.current_index] + self.nodes[int(node)].h:
                    self.nodes[int(node)].previous_node = self.current_index
                    self.nodes[int(node)].g = self.nodes[int(self.current_index)].g + self.nodes[int(node)].graph[self.current_index]
                    self.nodes[int(node)].f = self.nodes[int(node)].g + self.nodes[int(node)].h
    
        self.closed_nodes.append(self.open_nodes.pop(self.open_nodes.index(self.current_index)))
        acitve_f = []
        for node in self.open_nodes:
            acitve_f.append( self.nodes[int(node)].f)
        i = acitve_f.index(min(acitve_f))
        self.current_index = self.open_nodes[i]  

    def run(self):
        while str(self.end_index) not in list(self.nodes[int(self.current_index)].graph.keys()):
        # for i in range(6):   
            self.A_star_step()
            print(self.current_index)
            print(self.open_nodes)
            print(self.closed_nodes) 
        self.A_star_step()
        print(self.nodes[self.end_index].previous_node)


AS_ = A_star(nodes, 0, 15)
AS_.run()
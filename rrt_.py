import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
class RRT():   
    def __init__(self): 
        self.start_node = np.array([0,0,0])
        self.end_node = np.array([7,9,-1])
        self.points = np.array([self.start_node]) # array([[a1, b1, c1], [a2, b2, c2] ])
        self.obstacles = np.array([ [(8,3),2],
                                    [(2,1), 0.5],
                                    [(1,2), 0.5],
                                    [(5,5), 0.75],
                                    [(1,8), 1.5],
                                    [(9,9), 1],
                                    [(5,9), 0.75]
                                    ])                           
    
    def path_plan(self):
        c_node = np.array([100,100,0])
        r = np.sqrt((c_node[0]-self.end_node[0])**2 + (c_node[1]-self.end_node[1])**2)
        # for i in range(200):
        while r> .6:
            p = self.randompoint(self.points)
            p_index = self.closest_node(self.points, p)
            point = self.points[p_index][:2]
            c_node, col = self.next_node(point, p, p_index)
            c_node = np.append(c_node, p_index)
            r = np.sqrt((c_node[0]-self.end_node[0])**2 + (c_node[1]-self.end_node[1])**2)
            if col == False:
                self.points = np.append(self.points, np.array([c_node]), axis=0)

    def randompoint(self,points):
        a = np.random.uniform(0,10,[2]) # array([ a, b ])
        if  a not in points[:,:2]:
            return a # array([ a, b ])
        else:
            while a not in points[:,:2]:
                a = np.random.uniform(0,10,[2])
                if a not in points[:,:2]:
                    return a # array([ a, b ])

    def closest_node(self, points, node):
        p = node
        min_d = 11*np.sqrt(2)
        min_index = 9999
        for point in points[:,:2]:
            if np.sqrt((point[0]-p[0])**2 + (point[1]-p[1])**2) < min_d:
                min_d = ((point[0]-p[0])**2 + (point[1]-p[1])**2)
                a = np.where(np.all(points[:,:2] == point, axis=1))
                min_index = a[0][0]
        return min_index

    def next_node(self, e_node, n_point, index):
        vector = n_point - e_node # np.array([a1,a2]) - np.array([b1,b2])
        n = vector/np.linalg.norm(vector) # np.array([a1,a2])
        n_node = e_node + n*0.6
        np.append(n_node, index) # np.array([a1,a2,a3])             
        for obs in self.obstacles:
            r = np.sqrt( (obs[0][0]-n_node[0])**2 + (obs[0][1]-n_node[1])**2 ) - .2
            if r <= obs[1]:                
                return n_node, True        
        return n_node, False


rrt = RRT()
rrt.path_plan()  
print(rrt.points)

# Visualizing of RRT
plt.axes()
points = [
    [(8,3),2],
    [(2,1), 0.5],
    [(1,2), 0.5],
    [(5,5), 0.75],
    [(1,8), 1.5],
    [(9,9), 1],
    [(5,9), 0.75]
]

for point in points:
    x = point[0][0]
    y = point[0][1]
    radius = point[1]
    circle = plt.Circle((x,y), radius=radius, fc=(97/255,203/255,136/255, 0.5))
    plt.gca().add_patch(circle)

x=[]
y=[]
for point in rrt.points:
    x.append(point[0])
    y.append(point[1])

plt.scatter(x,y, s=15)
plt.axis('scaled') 
plt.grid()

#RRT Plot without smoothing
pp = np.array([[ rrt.points[-1,0], rrt.points[-1,1] ]])
# print(pp)
next_index = int(rrt.points[-1,2])
point_list = np.array([ pp[0] ])
while next_index != 0:
    pp = np.array([[ rrt.points[int(next_index), 0], rrt.points[int(next_index), 1] ]])
    point_list = np.append(point_list, pp, axis=0)
    next_index = int(rrt.points[next_index, 2])

xx = []
yy = []
for point in point_list:
    xx.append(point[0])
    yy.append(point[1])
plt.plot(xx,yy)
plt.show()

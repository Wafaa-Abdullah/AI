#!/usr/bin/env python
# coding: utf-8

# Task 1:

# In[3]:


dictt={"x":100,"y":200,"a":50,"b":300} 
sorted(dictt.keys())
for key in sorted(dictt.keys()) :
    print(key , " : " , dictt[key])


# Task 2:

# 1)adjacency List: An Adjacency list is an array consisting of the address of all the linked lists. The first node of the linked list represents the vertex and the remaining lists connected to this node represents the vertices to which this node is connected. This representation can also be used to represent a weighted graph. The linked list can slightly be changed to even store the weight of the edge.
# 2)Adjacency Matrix: Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.

# Task 3:

# BFS, Breadth-First Search:
# It is a technique for finding the shortest path in the graph, it uses the queue
# one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue.
# DFS, Depth First Search:
# It uses the Stack and performs two stages, first visited vertices are pushed into the stack, and second if there are no vertices then visited vertices are popped.

# In[32]:


#BFS implementation
#initialize graph with dictionary node:adjacency as input for bfs funcation
import queue
graph = {
  '2' : ['2','4'],
  '4' : ['2']
}
#list for visited node
visited = []
queue = []  

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
#loop for to visit each node to pop the node from queue
    while queue:          
        x = queue.pop(0) 
        print (x) 
#loop for visiting non visited node and push it in the visited list and queue 
        for neighbour in graph[x]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '2')   


# In[31]:


#DFS implementation
#initialize graph with dictionary node:adjacency as input for dfs funcation
graph = {
  '2' : ['2','3'],
  '3' : ['2']
}
# to put visited node 
visited = set()

def dfs(visited, graph, y):  
    if y not in visited:
        print (y)
        visited.add(y)
        for neighbour in graph[y]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, '3')


# Task 4:

# In[4]:


import lib
lib.x


# In[5]:


lib.maxx(2,3)


# In[6]:


lib.minn(4,5)


# In[8]:


lib.multiplte(2,5)


# In[9]:


lib.divide(4,2)


# In[10]:


lib.myList


# Task 5:

# In[ ]:


from queue import LifoQueue as stack 
s = stack()
def push_to_stack(l):
    for i in l:
        s.put(i)
l = input("Enter number of elements : ")
while s.qsize()!=0:
    push_to_stack(l)
print(s.qsize())


# Task 6:

# In[ ]:


#multiset


# In[ ]:


#unorderedset


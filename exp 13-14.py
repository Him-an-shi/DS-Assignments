'''13	Consider a particular area in your city. Note the popular locations A, B, C . . . in that area. 
Assume these locations represent nodes of a graph. If there is a route between two locations,
 it is represented as connections between nodes. Find out the sequence in which you will visit these locations, 
 starting from (say A) using (i) BFS and (ii) DFS. Represent a given graph using an adjacency matrix to perform DFS and BFS
14	Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
 Assume these locations represent nodes of a graph. If there is a route between two locations, 
 it is represented as connections between nodes. Find out the sequence in which you will visit these locations, 
 starting from (say A) using (i) BFS and (ii) DFS. Represent a given graph using adjacency list to perform DFS and BFS.  
'''
from collections import deque

def add_edges_mat(matrix,u,v):
    matrix[u][v]=1
    matrix[v][u]=1
    return matrix

def add_edges_list(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)
    return graph

def DFS_mat(matrix,start):
    traversal=[]
    stack=[start]
    visited=set()
    while stack:
        node=stack.pop()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
        for neighbour in range(len(matrix[node])):
            if matrix[node][neighbour]==1 and neighbour not in visited:
                stack.append(neighbour)
    return traversal[::-1]

def BFS_mat(matrix,start):
    traversal=[start]
    queue=deque([start])
    visited=set()
    visited.add(start)
    while queue:
        node=queue.popleft()
        for neighbour in range(len(matrix[node])):
            if matrix[node][neighbour]==1 and neighbour not in visited:
                visited.add(neighbour)
                traversal.append(neighbour)
                queue.append(neighbour)
    return traversal

def DFS_list(graph,start):
    traversal=[]
    stack=[start]
    visited=set()
    while stack:
        node=stack.pop()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
    return traversal[::-1]

def BFS_list(graph,start):
    traversal=[start]
    queue=deque([start])
    visited=set()
    visited.add(start)
    while queue:
        node=queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                traversal.append(neighbour)
                queue.append(neighbour)
    return traversal
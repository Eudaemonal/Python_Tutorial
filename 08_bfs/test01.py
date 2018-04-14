#!/usr/bin/python3

from collections import defaultdict
import random

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*(len(self.graph))

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__=="__main__":
    g = Graph()
    num_nodes = 8
    num_edges = 32

    for i in range(0, num_edges):
        from_node = random.randint(0,num_nodes)
        to_node = random.randint(0,num_nodes)

        g.addEdge(from_node, to_node)
        print("Add node from {} to {}".format(from_node, to_node))

    print("BFS path:")
    g.BFS(2)

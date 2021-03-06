# Graph Time Complexity - O(V+E)
# Space Complexity - O(V) for the stack/queue

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        # Implementation using adjacancy lists
        self.graph = defaultdict(list)
        
    def add_edge(self, source, destination):
        # Implementation for bidirectional graph
        self.graph[source].append(destination)
        self.graph[destination].append(source)
        
    def print_graph(self):
        print("Graph")
        for g in self.graph.items():
            print(g)
        
    def dfs(self, vertex, visited):
        print("DFS")
        stack = []
        # visited = set()
        stack.append(vertex)
        while stack:
            current = stack.pop()
            # if the current node is not visited then add it to stack
            if current not in visited:
                visited.add(current)
                print(current, end=' ')
            
            # traverse the current node and add it to stack if it is not visited
            for adj in self.graph[current]:
                if adj not in visited:
                    stack.append(adj)
    
    def bfs(self, vertex, visited):
        print("BFS")
        queue = deque()
        # visited = set()
        queue.append(vertex)
        
        while queue:
            current = queue.popleft()
            # if the current node is not visited then add it to queue
            if current not in visited:
                visited.add(current)
                print(current, end=' ')
        
            # traverse the current node and add it to stack if it is not visited
            for adj in self.graph[current]:
                if adj not in visited:
                    queue.append(adj)

    # for handling disconnected graph
    def dfs_disconnected_graph(self):
        visited = set()
        for v in self.graph:
            # if the vertex is not visited then traverse dfs for tht vertex
            if v not in visited:
                self.dfs(v, visited)

    def bfs_disconnected_graph(self):
        visited = set()
        for v in self.graph:
            # if the vertex is not visited then traverse bfs for tht graph
            if v not in visited:
                self.bfs(v, visited)

    def dfs_recursive(self, v, visited):
        visited.add(v)
        print(v, end='')
        
        for v in self.graph[v]:
            if v not in visited:
                self.dfs_recursive(v, visited)

    # for handling disconnected graph for recursive approach is same as iterative approach
    def dfs_recursive_disconnected(self):
        visited = set()
        for v in self.graph:
            if v not in visited:
                self.dfs_recursive(v, visited)
        # [self.dfs_recursive(v, visited) for v in self.graph if v not in visited]

g = Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,6)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(4,7)
g.add_edge(5,6)

# Start traversal from vertex 1
g.dfs(1,set())
g.bfs(1,set())

g.dfs_disconnected_graph()
g.bfs_disconnected_graph()

g.dfs_recursive(1, set())
g.dfs_recursive_disconnected()

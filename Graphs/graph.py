class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            
    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].remove(v2)
            self.adjacency_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for neighbour in self.adjacency_list[vertex]:
                self.adjacency_list[neighbour].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
      
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        
        while queue:
            current = queue.pop(0)
            print(current)
            for adjacent in self.adjacency_list[current]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)
                    
    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current)
            
            for adjacent in self.adjacency_list[current]:
                if adjacent not in visited:
                    stack.append(adjacent)


    def print(self):
        for vertex in self.adjacency_list:
            print(vertex , " : ", self.adjacency_list[vertex])
        print('\n')
            
            
g = Graph()
g.add_vertex(1) 
g.add_vertex(2) 
g.add_vertex(3) 
g.add_vertex(4)

g.add_edge(1, 2) 
g.add_edge(3, 2) 
g.add_edge(4, 2) 
g.add_edge(1, 3) 

g.print()

g.bfs(2)
g.dfs(2)


      
        
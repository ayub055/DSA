class Solution:
    def bfs(self, grid, visited, r, c):
        rows, cols = len(grid), len(grid[0])
        queue = [(r, c)]
        visited.add((r, c))
        
        while queue:
            row, col = queue.pop(0)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                
                if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c)  not in visited:
                    queue.append((r, c))
                    visited.add((r, c))         
    
    def numIslands(self, grid):
        if grid is None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    self.bfs(grid, visited, r, c)
                    num_islands += 1
                    
        return num_islands
    
    def maxAreaOfIsland(self, grid):
        pass
                        
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# q = [(1, 2), (1, 4)]
# print(q.pop())
s = Solution()
print(s.numIslands(grid))


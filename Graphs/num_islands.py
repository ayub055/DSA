class Solution:
    def bfs(self, grid, visited, r, c, area):
        
        rows = len(grid)
        cols = len(grid[0])
        queue = [(r, c)]
        visited.add((r, c))
        
        while queue:
            row, col = queue.pop(0)
            area += 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                
                if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] != 0:
                    queue.append((r, c))
                    visited.add((r, c))
                    
        return area
                    
                       
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
        if grid is None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    area = self.bfs(grid, visited, r, c, area)
                    maxArea = max(area, maxArea)
                    count += 1
                    
        return maxArea, count
                    
    
   
                        
    
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
print(s.maxAreaOfIsland(grid))


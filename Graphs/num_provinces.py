class Solution:
    def bfs(self, v, adj_list, visited):
        visited[v] = 1
        queue = [v]
        
        while queue:
            curr = queue.pop(0)
            adj = adj_list[curr]
            print(curr, adj)
            for i in range(len(adj)):
                if visited[adj[i]] != 1:
                    visited[adj[i]] = 1
                    queue.append(adj[i])
        
        return visited
        
        
    def numProvinces(self, adj):
        adjacency_list = {}
        
        for row in range(len(adj)):
            adjacency_list[row] = []
            for col in range(len(adj)):
                if adj[row][col] == 1 and row != col:
                    adjacency_list[row].append(col)
        print(adjacency_list)
        
        # import sys; sys.exit()
        visited = [0] * len(adj)
        count = 0
        for i in range(len(adj)):
            # print(visited)
            if not visited[i]:
                visited = self.bfs(i, adjacency_list, visited)
                count += 1
        return count
    
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
    
        

sol = Solution()
# adj = [[1, 0, 1],
#        [0, 1, 0],
#        [1, 0, 1]]  

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numProvinces(grid))



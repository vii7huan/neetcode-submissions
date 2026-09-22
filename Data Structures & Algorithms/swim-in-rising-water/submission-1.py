class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = {(0,0)}
        heap = [(grid[0][0],0,0)] # there is a tuple
        while heap:
            t,r,c = heapq.heappop(heap)
            if r == n-1 and c == n-1 :
                return t
            for dr, dc, in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+ dr, c+ dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited: 
                    #nr, nc order....
                    visited.add((nr,nc))
                    heapq.heappush(heap, (max(t,grid[nr][nc]), nr,nc))

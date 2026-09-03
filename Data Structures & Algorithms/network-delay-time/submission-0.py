class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #an algorithm for finding the shortest paths between nodes in a weighted graph,
        #which may represent, for example, a road network.

        #minheap [path,node]:
        
    
        adj = defaultdict(list)
        for u, v, w in times: #times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        q = deque([(k, 0)])
        dist[k] = 0

        while q:
            node, time = q.popleft()
            if dist[node] < time:
                continue
            for nei, w in adj[node]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))

        res = max(dist.values())
        return res if res < float('inf') else -1
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # Track minimum distance from the current MST to each unvisited vertex
        min_dist = [float('inf')] * n
        min_dist[0] = 0  # Start from vertex 0
        
        visited = [False] * n
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            # Find the unvisited vertex with the smallest min_dist
            curr = -1
            curr_min = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_min:
                    curr_min = min_dist[i]
                    curr = i

            # Add the cost to our total MST weight
            total_cost += curr_min
            visited[curr] = True
            edges_used += 1

            # Update min_dist for all remaining unvisited vertices using the newly added vertex
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[curr][0] - points[v][0]) + abs(points[curr][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return total_cost
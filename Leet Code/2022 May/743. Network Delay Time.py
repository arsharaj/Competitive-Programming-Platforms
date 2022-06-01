import collections

class Solution:
    def networkDelayTime(self, edge_list, N, K):
        # Build Graph
        graph = collections.defaultdict(list)
        for src, dest, cost in edge_list:
            graph[src].append((dest, cost))
        
        # Apply Djikstra's Algorithm
        priority_queue = [(0, K)]
        visited = set()
        max_cost = 0
        while priority_queue:
            cost, node = collections.heapq.heappop(priority_queue)
            if node not in visited:
                visited.add(node)
                max_cost = max(max_cost, cost)
                for neighbour, new_cost in graph[node]:
                    if neighbour not in visited:
                        collections.heapq.heappush(priority_queue, (cost + new_cost, neighbour))
        
        # Return Processed Values
        if len(visited) == N:
            return max_cost
        else:
            return -1
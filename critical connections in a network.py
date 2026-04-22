from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        discovery_time = [-1] * n
        low_link = [-1] * n
        bridges = []
        self.time = 0
        
        def dfs(node, parent):
            discovery_time[node] = low_link[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if discovery_time[neighbor] == -1:
                    dfs(neighbor, node)
                    low_link[node] = min(low_link[node], low_link[neighbor])
                    if low_link[neighbor] > discovery_time[node]:
                        bridges.append([node, neighbor])
                else:
                    low_link[node] = min(low_link[node], discovery_time[neighbor])
                    
        dfs(0, -1)
        return bridges

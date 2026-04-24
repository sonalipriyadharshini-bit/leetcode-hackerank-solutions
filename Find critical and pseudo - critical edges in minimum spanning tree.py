class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Add index
        new_edges = [edges[i] + [i] for i in range(len(edges))]
        new_edges.sort(key=lambda x: x[2])

        # DSU (Union-Find)
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            px, py = find(parent, x), find(parent, y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True

        # Kruskal function
        def kruskal(exclude, include):
            parent = list(range(n))
            rank = [0] * n
            weight = 0

            # force include edge
            if include != -1:
                u, v, w, _ = new_edges[include]
                if union(parent, rank, u, v):
                    weight += w

            for i, (u, v, w, _) in enumerate(new_edges):
                if i == exclude:
                    continue
                if union(parent, rank, u, v):
                    weight += w

            # check if MST formed
            root = find(parent, 0)
            if all(find(parent, i) == root for i in range(n)):
                return weight
            return float('inf')

        # Step 1: original MST weight
        mst_weight = kruskal(-1, -1)

        critical = []
        pseudo = []

        # Step 2: test each edge
        for i in range(len(new_edges)):
            # check critical
            if kruskal(i, -1) > mst_weight:
                critical.append(new_edges[i][3])
            # check pseudo-critical
            elif kruskal(-1, i) == mst_weight:
                pseudo.append(new_edges[i][3])

        return [critical, pseudo]

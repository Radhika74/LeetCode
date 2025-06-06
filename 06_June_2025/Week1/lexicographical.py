class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(97, 123)}  # a-z

        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return
            if rootA < rootB:
                parent[rootB] = rootA
            else:
                parent[rootA] = rootB

        for a, b in zip(s1, s2):
            union(a, b)

        return ''.join(find(c) for c in baseStr)

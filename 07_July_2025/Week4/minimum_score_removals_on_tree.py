class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        in_time = [0] * n
        out_time = [0] * n
        subtree_xor = [0] * n
        time = 0

        def dfs(node, parent):
            nonlocal time
            time += 1
            in_time[node] = time
            xor_val = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    xor_val ^= dfs(nei, node)
            out_time[node] = time
            subtree_xor[node] = xor_val
            return xor_val

        total_xor = dfs(0, -1)
        result = float('inf')
        
        for a in range(n):
            for b in range(a + 1, n):
                if a == 0 or b == 0:
                    continue  

                def is_descendant(u, v):
                    return in_time[v] <= in_time[u] <= out_time[u] <= out_time[v]

                if is_descendant(a, b):
                    xor1 = subtree_xor[a]
                    xor2 = subtree_xor[b] ^ subtree_xor[a]
                    xor3 = total_xor ^ subtree_xor[b]
                elif is_descendant(b, a):
                    xor1 = subtree_xor[b]
                    xor2 = subtree_xor[a] ^ subtree_xor[b]
                    xor3 = total_xor ^ subtree_xor[a]
                else:
                    xor1 = subtree_xor[a]
                    xor2 = subtree_xor[b]
                    xor3 = total_xor ^ xor1 ^ xor2

                result = min(result, max(xor1, xor2, xor3) - min(xor1, xor2, xor3))

        return result

        
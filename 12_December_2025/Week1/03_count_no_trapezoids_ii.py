# class Solution:
#     def countTrapezoids(self, pts: List[List[int]]) -> int:
#         g1 = defaultdict(list)
#         g2 = defaultdict(list)

#         for i, (x1, y1) in enumerate(pts):
#             for x2, y2 in pts[:i]:
#                 dy = y1 - y2
#                 dx = x1 - x2
#                 s = dy / dx if dx else float('inf')
#                 k = (y1 * dx - x1 * dy) / dx if dx else x1
#                 g1[s].append(k)
#                 g2[(x1 + x2, y1 + y2)].append(s)
#         res = 0
#         for L in g1.values():
#             if len(L) < 2:
#                 continue
#             cur = 0
#             for c in Counter(L).values():
#                 res += cur * c
#                 cur += c
#         for L in g2.values():
#             if len(L) < 2:
#                 continue
#             cur = 0
#             for c in Counter(L).values():
#                 res -= cur * c
#                 cur += c
#         return res
def fun(k, arr):
    so = sum(arr)
    for i in range(1,k):
        s=0
        for j in arr:
            s+= i^j
        if s>so:
            so=s
    return so
n=3
k=7
arr=[1,6,3]
print(fun(k,arr)) 
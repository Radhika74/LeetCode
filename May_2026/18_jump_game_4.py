class Solution:
    def minJumps(self, a: List[int]) -> int:
        g,curs,visited,step = defaultdict(list),[0],{0},0
        for i,v in enumerate(a): g[v].append(i)

        while curs:
            nex = []
            for i in curs:
                if i==len(a)-1: return step
                for j in chain([i-(i>0),i+(i<len(a))],a[i] in g and g.pop(a[i]) or []):
                    if j not in visited: visited.add(j); nex.append(j)

            curs,step = nex,step+1

        return -1
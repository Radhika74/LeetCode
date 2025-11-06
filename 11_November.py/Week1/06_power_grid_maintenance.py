class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        components = dict()
        node_component = dict()
        adjlist = dict()

        for connection in connections:
            x = connection[0]
            y = connection[1]

            if x in adjlist:
                adjlist[x].append(y)
            else:
                adjlist[x] = []
                adjlist[x].append(y)

            if y in adjlist:
                adjlist[y].append(x)
            else:
                adjlist[y]=[]
                adjlist[y].append(x)
        
        visited = set()
        def dfs(component_id, node):
            components[component_id].add(node)
            node_component[node] = component_id
            visited.add(node)
            for nb in adjlist.get(node,[]):
                if nb in visited:
                    continue

                dfs(component_id,nb)
            
        component_id = 0
        for i in range(1, c+1):
            if i not in visited:
                components[component_id] = SortedSet()
                dfs(component_id, i)
                component_id+=1

        result = []
        for q in queries:
            operation = q[0]
            target = q[1]
            component_id = node_component.get(target,-1)
            if component_id == -1:
                continue

            if operation == 2:   
                if target in components[component_id]:
                    components[component_id].discard(target)
            else:
                if target in components[component_id]:
                    result.append(target)
                else:
                    if len(components[component_id]) > 0:
                        result.append(components[component_id][0])
                    else:
                        result.append(-1)

        return result        
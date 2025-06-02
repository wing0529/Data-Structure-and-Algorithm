from collections import deque

def breath_first_search(graph,root):
    visited =[]
    discovered=[]
    queue = deque([root])
    discovered.append(root)

    while len(queue)>0:
        node = queue.popleft()
        visited.append(node)
        print(graph[node])
        undiscovered=set(graph[node]).difference(set(discovered))
        print(undiscovered)

        if len(undiscovered)>0:
            for elem in sorted(undiscovered):
                queue.append(elem)
                discovered.append(elem)

    return visited


graph1 = {
    'A':['B','G','D'],
    'B':['A','F','E'],
    'C':['F','H'],
    'D':['F','A'],
    'E':['B','G'],
    'F':['B','D','C'],
    'G':['A','E'],
    'H':['C'],

}

ans = breath_first_search(graph1,'A')
print(*ans,sep='-')
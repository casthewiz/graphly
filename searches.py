def dfs(g, v):
    # g is a graph object
    # v is start node
    visited = set()
    stack = [v]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            #do relevant function call here
            #add to stack vertexes in visited node
            stack.extend(set(g[vertex]).difference(visited))
    return {v : list(visited)}


def bfs(g, v):
    # g is a graph object
    # v is start node
    visited = set()
    queue = [v]
    while queue:
        vertex = queue.pop(0)
        # and just like that, our list works like a queue!
        if vertex not in visited:
            visited.add(vertex)
            #do relevant function call here
            #add to queue vertexes in visited node
            queue.extend(set(g[vertex]).difference(visited))
    return visited

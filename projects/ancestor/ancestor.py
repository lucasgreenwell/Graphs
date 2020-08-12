#helper graph class, don't need it all and the search has to be different
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    #adds a directed edge so that inheritance is represented
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)



def earliest_ancestor(ancestors, starting_node):
    #makes a directed graph
    graph_of_ancestors = Graph()
    #fills it with stuff
    for pair in ancestors:
        graph_of_ancestors.add_vertex(pair[0])
        graph_of_ancestors.add_vertex(pair[1])
        graph_of_ancestors.add_edge(pair[1], pair[0])
    #sets up variables for the longest path that we've seen and the node at the end of that path
    max_path_len = 1
    #needs to return -1 if no parents are available
    earliest_ancestor = -1
    #queue for breadth first search
    queue = []
    #breadth first search, slight changes for deepest found node
    queue.append([starting_node])
    while len(queue) > 0:
        path = queue.pop(0)
        v = path[-1]
        if (len(path) == max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph_of_ancestors.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.append(path_copy)
    return earliest_ancestor








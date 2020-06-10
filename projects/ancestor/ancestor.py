from graph import Graph

from util import Stack


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for s in ancestors:
        # print(s[0],s[1])
        g.add_vertex(s[0])
        g.add_vertex(s[1])
        g.add_edge(s[1],s[0])
    
    s = Stack()
    s.push([starting_node])
    visited= set()
    
    while s.size() > 0:
        path = s.pop()
        current = path[-1]
        if current not in visited:
            visited.add(current)

            for neighbor in g.get_neighbors(current):
                path_copy = list(path)
                path_copy.append(neighbor)
                s.push(path_copy)
    if path[-1] == starting_node:
        return -1
    
    return min(g.get_neighbors(path[-2]))
if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors,8))
    
    
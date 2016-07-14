class Node:
    def __init__(self, value, neighbors = []):
        self.value = value
        self.neighbors = neighbors
        self.marked = False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

def breadth_first_search(n):
    queue = []
    n.marked = True
    queue.append(n)

    while queue:
        n = queue.pop(0)
        print n.value
        for neighbor in n.neighbors:
            if not neighbor.marked:
                neighbor.marked = True
                queue.append(neighbor)

# assuming we're searching for a value and
# that all values in the graph are unique
def routeExists(root, dest_val):
    queue = []
    root.marked = True
    queue.append(root)

    while queue:
        n = queue.pop(0)
        if n.value == dest_val:
            return True
        for neighbor in n.neighbors:
            # print str.format("value: {}, marked: {}", neighbor.value, neighbor.marked)
            if not neighbor.marked:
                neighbor.marked = True
                queue.append(neighbor)
    return False

n = Node(1, [Node(2), Node(3)])
# print breadth_first_search(n)
print routeExists(n, 3)
n = Node(1, [Node(2, [Node(5, [Node(6)])]), Node(3)])
n.neighbors[1].neighbors.append(n)
print routeExists(n, 6)

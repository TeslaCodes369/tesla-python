class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.adjList = []
        self.visited = False


def DFS(start):
    stack = [start]

    while stack:
        node = stack.pop()
        node.visited = True
        print(node.name)

        for nd in reversed(node.adjList):
            if not nd.visited:
                stack.append(nd)


def DFS_RE(start):
    if start.visited:
        return

    print(start.name)
    start.visited = True

    for nd in start.adjList:
        DFS_RE(nd)


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')

    A.adjList.append(B)
    B.adjList.append(A)
    A.adjList.append(C)
    C.adjList.append(A)
    A.adjList.append(D)
    D.adjList.append(A)
    D.adjList.append(E)
    E.adjList.append(D)

    DFS(A)
    # DFS_RE(A)

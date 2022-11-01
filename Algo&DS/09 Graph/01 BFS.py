class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.adjList = []
        self.visited = False


def BFS(node):
    qu = [node]
    while qu:
        nd = qu.pop(0)
        nd.visited = True
        print(nd.name)

        for n in nd.adjList:
            if not n.visited:
                qu.append(n)


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

    BFS(E)

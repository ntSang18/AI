class Tree:
    def __init__(self, label, value=10000):
        self.label = label
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __lt__(self, other):
        return self.value < other.value

# Chiến lược cho người chơi max
def MaxValue(node):
    if len(node.children) == 0:
        return node
    node.value = -10000
    for child in node.children:
        temp = MinValue(child)
        if temp.value > node.value:
            node.value = temp.value
    return node

# Chiến lược cho người chơi min
def MinValue(node):
    if len(node.children) == 0:
        return node
    node.value = 10000
    for child in node.children:
        temp = MaxValue(child)
        if temp.value < node.value:
            node.value = temp.value
    return node


def MiniMax_Search(state):
    MaxValue(state)


if __name__ == '__main__':
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5
    MiniMax_Search(A)
    print(A.value)

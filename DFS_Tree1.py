from sympy import false


class Node:

    def __init__(self, name):
        self.Name = name
        self.Children = []

    def addChild(self, list):
        for c in list:
            self.Children.append(c)


def BFS(initialState: Node, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)
        if goal == state.Name:
            return explored
        for neighbor in state.Children:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return false


if __name__ == '__main__':
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    nodeL = Node("L")
    nodeM = Node("M")
    nodeN = Node("N")
    nodeO = Node("O")
    nodeA.addChild([nodeB, nodeC])
    nodeB.addChild([nodeD, nodeE])
    nodeC.addChild([nodeF, nodeG])
    nodeD.addChild([nodeH, nodeI])
    nodeE.addChild([nodeJ, nodeK])
    nodeF.addChild([nodeL, nodeM])
    nodeG.addChild([nodeN, nodeO])
    result = BFS(nodeA, 'H')
    if result:
        s = "explored: "
        for i in result:
            s += i.Name + ''
            print(s)
    else:
        print("404 Not Found!")

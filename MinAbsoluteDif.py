def getMinimumDifference(root):
    numList = [root.val]

    def addNode(node):
        if node.left is None and node.right is None:
            return

        if node.left is not None:
            numList.append(node.left.val)
            addNode(node.left)
        if node.right is not None:
            numList.append(node.right.val)
            addNode(node.right)


    addNode(root)

    numList.sort()

    minDifference = numList[1] - numList[0]

    for i in range(2, len(numList)):
        minDifference = min(minDifference, numList[i] - numList[i-1])

    return minDifference

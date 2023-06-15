def maxLevelSum(root):
    levels = {1: root.val}

    def addNode(node, depth):
        if node.left is None and node.right is None:
            return

        if depth not in levels:
            levels[depth] = 0

        if node.left is not None:
            levels[depth] += node.left.val
            addNode(node.left, depth + 1)

        if node.right is not None:
            levels[depth] += node.right.val
            addNode(node.right, depth + 1)

    addNode(root, 2)

    return max(levels, key=levels.get)

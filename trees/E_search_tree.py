# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:

    def _maxValue(node):
        if node is None:
            return 0
        leftMax = _maxValue(node.left)
        rightMax = _maxValue(node.right)
        value = 0
        if leftMax > rightMax:
            value = leftMax
        else:
            value = rightMax

        if value < node.value:
            value = node.value
        return value

    def _minValue(node):
        if node is None:
            return 1000000000
        leftMax = _minValue(node.left)
        rightMax = _minValue(node.right)
        value = 0
        if leftMax < rightMax:
            value = leftMax
        else:
            value = rightMax

        if value > node.value:
            value = node.value
        return value

    if root is None:
        return True
    if (root.left is not None and _maxValue(root.left) >= root.value):
        return False
    if (root.right is not None and _minValue(root.right) <= root.value):
        return False
    if (solution(root.left) is False or solution(root.right) is False):
        return False
    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()

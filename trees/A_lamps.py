# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if root is None:
        return float('-inf')
    start = root.value
    left = solution(root.left)
    right = solution(root.right)
    if start < left:
        start = left
    if start < right:
        start = right
    return start


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()

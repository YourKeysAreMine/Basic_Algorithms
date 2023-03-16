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
    def _get_height(root):
        if root is None:
            return 0
        return 1 + max(_get_height(root.left), _get_height(root.right))

    if root is None:
        return True
    return solution(root.right) and (
        solution(root.left) and abs(_get_height(root.left) -
                                    _get_height(root.right)) <= 1
    )


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
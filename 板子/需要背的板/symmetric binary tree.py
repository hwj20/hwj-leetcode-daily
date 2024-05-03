class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return isMirror(left.left, right.right) and isMirror(left.right, right.left)

# Example usage:
if __name__ == "__main__":
    # Constructing a symmetric binary tree:
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print("Is the binary tree symmetric?:", isSymmetric(root))

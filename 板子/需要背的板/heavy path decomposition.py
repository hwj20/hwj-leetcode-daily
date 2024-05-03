class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

def heavy_light_decomposition(root):
    """ Computes sizes of subtrees and performs heavy-light decomposition. """
    def dfs_size(node):
        """ Calculate size of each subtree and identify heavy child. """
        size = 1
        max_c_size = 0
        heavy_child = None
        for child in node.children:
            c_size = dfs_size(child)
            size += c_size
            if c_size > max_c_size:
                max_c_size = c_size
                heavy_child = child
        sizes[node] = size
        heavy[node] = heavy_child
        return size

    def decompose(node, head):
        """ Decompose the tree into heavy and light edges, and assign heads. """
        path_head[node] = head
        if heavy[node]:
            decompose(heavy[node], head)
        for child in node.children:
            if child != heavy[node]:
                decompose(child, child)

    sizes = {}
    heavy = {}
    path_head = {}

    dfs_size(root)
    decompose(root, root)
    
    return path_head, heavy

# Example usage
if __name__ == "__main__":
    # Constructing a tree
    #        1
    #       / \
    #      2   3
    #     /|   \
    #    4 5    6
    #          / \
    #         7   8
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node1.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6]
    node6.children = [node7, node8]

    path_head, heavy = heavy_light_decomposition(node1)
    
    # Outputting heavy paths
    for node, head in path_head.items():
        print(f"Node {node.val} is in the path headed by {head.val}")

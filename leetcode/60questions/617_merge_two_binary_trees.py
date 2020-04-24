class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return None
            a = node1 if node1 else TreeNode(0)
            b = node2 if node2 else TreeNode(0)

            node = TreeNode(a.val + b.val)
            node.left = dfs(a.left, b.left)
            node.right = dfs(a.right, b.right)
            return node

        root = dfs(t1, t2)
        return root

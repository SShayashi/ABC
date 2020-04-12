# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'val:{self.val}'


class Solution:
    ans = True

    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(parent: TreeNode = None, current: TreeNode = None, is_l=None, is_r=None):
            if current is None:
                return
            # root node のとき
            if parent is None:
                dfs(parent=current, current=current.left, is_l=True)
                dfs(parent=current, current=current.right, is_r=True)
            if is_r:
                if parent.val >= current.val:
                    self.ans = False
            if is_l:
                if parent.val <= current.val:
                    self.ans = False
            dfs(parent=current, current=current.left, is_l=True)
            dfs(parent=current, current=current.right, is_r=True)

        dfs(current=root)
        return self.ans


def create_input(arr):
    length = len(arr)

    def create_node(i):
        if i >= length:
            return None
        if arr[i] is None:
            return None
        x = TreeNode(arr[i])
        x.left = create_node(i + i + 1)
        x.right = create_node(i + i + 2)
        return x

    return create_node(0)


case1 = create_input([5, 1, 4, None, None, 3, 6])
case2 = create_input([10, 5, 15, None, None, 6, 20])
x = Solution()

print(x.isValidBST(case2))

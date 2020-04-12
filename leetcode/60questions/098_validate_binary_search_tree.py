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
        def dfs(current, upper, lower):
            if current is None:
                return
            if not(lower < current.val < upper):
                self.ans = False
                return
            dfs(current.left, min(upper, current.val), lower)
            dfs(current.right, upper, max(lower, current.val))
            return
        dfs(current=root, upper=2**32, lower=-(2**32))
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

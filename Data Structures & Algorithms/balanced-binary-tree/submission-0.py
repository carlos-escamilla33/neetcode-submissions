# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(node):
            if node is None:
                return 0  # base case: empty subtree has height 0

            left = dfs(node.left)
            right = dfs(node.right)

            # if either subtree is already unbalanced, bubble -1 up
            if left == -1 or right == -1:
                return -1

            # if THIS node violates the balance condition, signal unbalanced
            if abs(left - right) > 1:
                return -1

            # otherwise return the true height of this subtree
            return 1 + max(left, right)

        return dfs(root) != -1
        
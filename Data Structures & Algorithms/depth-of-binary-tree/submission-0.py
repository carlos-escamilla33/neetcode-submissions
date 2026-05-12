# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def helper(node, curr_depth):
            if node is None:
                nonlocal max_depth
                max_depth = max(max_depth, curr_depth)
                return
            
            curr_depth += 1
            helper(node.left, curr_depth)
            helper(node.right, curr_depth)

        helper(root, 0)

        return max_depth
                
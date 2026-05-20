# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(nodeP, nodeQ):
            if nodeQ is None and nodeP is None:
                return True
            if (nodeP is None and nodeQ) or (nodeQ is None and nodeP):
                return False
            if nodeP.val != nodeQ.val:
                return False
            
            left_traversal = dfs(nodeP.left, nodeQ.left)
            right_traversal = dfs(nodeP.right, nodeQ.right)

            if left_traversal and right_traversal:
                return True
            return False

        res = dfs(p, q)

        return res
        
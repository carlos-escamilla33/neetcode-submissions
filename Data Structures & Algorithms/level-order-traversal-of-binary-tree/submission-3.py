# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        queue = [[root]]

        while queue:
            node_arr = queue.pop(0)
            temp_arr = []
            curr_arr = []
            for i in range(len(node_arr)):
                node = node_arr[i]
                temp_arr.append(node.val)
                if node.left:
                    curr_arr.append(node.left)
                if node.right:
                    curr_arr.append(node.right)
            if curr_arr:
                queue.append(curr_arr)
            res.append(temp_arr)
        
        return res
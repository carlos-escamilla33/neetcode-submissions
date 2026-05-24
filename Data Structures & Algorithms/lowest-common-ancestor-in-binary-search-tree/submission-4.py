# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
    


"""
Goal: find the lowest common ancestor is a node that sits either between both nodes or if like in case example tw
    it doesnt have a node between them so we return the highest node

what do we return if the tree is not valid?
- There will always be at least 2
so if there is no node sitting between both we return the highest node? 
- Yeah so we want to return the node that is higher that is a decendant (can be itself) 
*** remember a bst has a value to the right of it that is greater and to the left that is less than
 
 ---------
- depth first search problem
- breadth first search problem ***

conditions are
- if the current node has to the left of it p/q and to the right of it p/q
    return the current node
- if the current node is p and qFound is false:
    return p
- if the curernt node is q and pFound is false:
    return q

- if the current node has a left:
    add to the queue
- if the current node has a right:
    add to the queue
"""
        
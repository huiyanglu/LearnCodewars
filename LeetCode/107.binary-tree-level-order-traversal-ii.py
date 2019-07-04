#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def bfs(root,level):
            if root != None:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(root.val)
                bfs(root.left,level + 1)
                bfs(root.right,level + 1)
        bfs(root,0)
        ans.reverse()
        return ans


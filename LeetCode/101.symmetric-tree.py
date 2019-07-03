#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def judge(p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            if p and q and p.val == q.val:
                return judge(p.left, q.right) and judge(p.right, q.left)
            return False
        return judge(root, root)



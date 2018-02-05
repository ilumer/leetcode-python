# coding:utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumLeftLeaves(root, False)

    # python中没有重载
    def sumLeftLeaves(self, root, flag=False):
        if not root:
            return 0
        if not root.left and not root.right:
            if flag:
                return root.val
            else:
                return 0
        return self.sumLeftLeaves(root.left, True) + \
            self.sumLeftLeaves(root.right, False)

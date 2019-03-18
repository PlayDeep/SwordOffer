# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return False
        if not pRoot.right or not pRoot.left:
            return False
        if pRoot.right.val == pRoot.left.val:
            return self.A_isSymmetrical_B(pRoot.right, pRoot.left)
        return False

    def A_isSymmetrical_B(self, treea, treeb):
        if not treea and not treeb:
            return True
        if treea and treeb:
            if treea.val == treeb.val:
                if treea.right and treeb.right and treea.left and treeb.left:
                    return self.A_isSymmetrical_B(treea.right, treeb.left) and self.A_isSymmetrical_B(treea.left,
                                                                                                      treeb.right)
                else:
                    return False
            else:
                return False
        return False

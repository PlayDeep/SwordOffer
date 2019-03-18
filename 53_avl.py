# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        left = self.get_depth(pRoot.left)
        right = self.get_depth(pRoot.right)
        if left - right == 1 or left - right == -1:
            return True
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def get_depth(self, pRoot):
        right = 0
        left = 0
        if not pRoot:
            return 0
        if pRoot.right != None:
            right = self.get_depth(pRoot.right)
        if pRoot.left != None:
            left = self.get_depth(pRoot.left)
        return left + 1 if left > right else right + 1


class Solution2:
    k = True
    def IsBalanced_Solution(self, pRoot):
        self.is_balanced(pRoot)
        return self.k

    def is_balanced(self, root):
        if root == None:
            return 0
        left = self.is_balanced(root.left)
        right = self.is_balanced(root.right)
        print left, right
        if abs(left -  right) > 1:
            self.k = False
        return left + 1 if left > right else right + 1






def listcreattree(root,llist,i):###用列表递归创建二叉树，
    # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
    # 再接着创建b的右子树，
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # print('列表序号：'+str(i)+' 二叉树的值：'+str(root.val))
            # 往左递推
            root.left = listcreattree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listcreattree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            # print('************返回根：',root.val)
            return root  ###这里的return很重要
    return root


def PrintFromTopToBottom(root):
    print "PrintFromTopToBottom"
    if not root:
        return []
    res = []
    queue = []
    queue.append(root)
    while (queue):
        res.append(queue[0].val)
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue.pop(0)
    print res
    return res

def main():
    a = Solution2()
    root = listcreattree(0, [1,2,3,4,5,6,7], 0)
    PrintFromTopToBottom(root)
    res = a.IsBalanced_Solution(root)
    print(res)


if __name__ == '__main__':
    main()
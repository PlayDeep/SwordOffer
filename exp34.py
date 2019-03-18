
# -*- coding:utf-8 -*-
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        if not root or not expectNumber:
            return None
        path = []
        cur_sum = 0
        self.find(root, expectNumber, path, cur_sum)

        return self.res


    def find(self, root, expectNumber, path, cur_sum):
        path.append(root.val)
        cur_sum += path[-1]
        is_leaf = root.left is None and root.right is None
        if is_leaf and cur_sum == expectNumber:
            # print path
            self.res.append(copy.deepcopy(path))
            # print self.res
        if root.left != None:
            self.find(root.left, expectNumber, path, cur_sum)
        if root.right != None:
            self.find(root.right, expectNumber, path, cur_sum)
        cur_sum -= path[-1]
        path.pop()

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
    a = Solution()
    root = listcreattree(0, [10, 5, 12, 4, 7], 0)
    PrintFromTopToBottom(root)
    expect = 22
    res = a.FindPath(root, expect)
    print(res)


if __name__ == '__main__':
    main()
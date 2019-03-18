# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    res = []
    def Print(self, pRoot):
        if pRoot == None:
            return None
        queue = []
        queue.append(pRoot)
        nextlevel = 0
        to_be_printed = 1
        res = []
        while(len(queue) > 0):
            pnode = queue[0]
            if pnode.left:
                queue.append(pnode.left)
                nextlevel += 1
            if pnode.right:
                queue.append(pnode.right)
                nextlevel += 1
            to_be_printed -= 1
            res.append(queue.pop(0).val)
            if to_be_printed == 0:
                self.res.append(res)
                res = []
                to_be_printed = nextlevel
                nextlevel = 0
        return self.res


def listcreattree(root,llist,i):###用列表递归创建二叉树，
    #它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
    #再接着创建b的右子树，
    if i<len(llist):
        if llist[i] =='#':
            return None ###这里的return很重要
        else:
            root=TreeNode(llist[i])
            # print('列表序号：'+str(i)+' 二叉树的值：'+str(root.val))
            #往左递推
            root.left=listcreattree(root.left,llist,2*i+1)#从根开始一直到最左，直至为空，
            #往右回溯
            root.right=listcreattree(root.right, llist,2*i+2)#再返回上一个根，回溯右，
            #再返回根'
            # print('************返回根：',root.val)
            return root  ###这里的return很重要
    return root

def main():
    a = Solution()
    root = listcreattree(0, [8,6,10,5,7,9,11], 0)
    res = a.Print(root)
    print(res)


if __name__ == '__main__':
    main()
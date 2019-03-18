# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        p_last_node = None
        p_last_node = self.convert_func(pRootOfTree, p_last_node)
        p_head_node = p_last_node
        while (p_head_node and p_head_node.left):
            p_head_node = p_head_node.left
        return p_head_node

    def convert_func(self, tree, p_last):
        if tree == None:
            return p_last
        cur_node = tree
        # 处理左子树
        if cur_node.left != None:
            p_last = self.convert_func(cur_node.left, p_last)
        # 连接左子树和根
        cur_node.left = p_last
        if p_last != None:
            p_last.right = cur_node
        p_last = cur_node
        # 处理右子树
        if cur_node.right != None:
            p_last = self.convert_func(cur_node.right, p_last)
        return p_last


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
    root = listcreattree(0, [10,6,14,4,8,12,16], 0)
    # PrintFromTopToBottom(root)
    expect = 22
    res = a.Convert(root)
    print(res)


if __name__ == '__main__':
    main()
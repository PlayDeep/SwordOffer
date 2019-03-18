# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head.val is None or not k:
            return None
        res = []
        p_node = head
        while (p_node.next):
            res.append(p_node)
            p_node = p_node.next

        return res[-k]


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def FindKthToTail(self, head, k):
        res = []
        while head != None:
            res.append(head)
            head = head.next
        if k>len(res) or k<1:
            return
        return res[-k]

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution3:
    def FindKthToTail(self, head, k):
        if head is None or k==0:
            return None
        index1 = head
        for _ in range(k-1):
            if index1.next:
                index1 = index1.next
            else:
                return None
        index2 = head
        while(index1.next != None):
            index1 = index1.next
            index2 = index2.next

        print(index2.val)
        return index2


def generate_node(arr):
    if arr < 1:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_node(head):
    p = head
    while p:
        print "print_node",p.val
        p = p.next

def main():
    a = Solution3()
    list_node = generate_node([1,2,3,4,5])
    res = a.FindKthToTail(list_node, 1)
    print_node(res)


if __name__ == '__main__':
    main()
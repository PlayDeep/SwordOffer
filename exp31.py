# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV or len(pushV) != len(popV):
            return
        stack = []
        for i in range(len(popV)):
            if stack and stack[-1] == popV[i]:
                stack.pop()
                continue
            if popV[i] not in pushV:
                return False
            stack.extend(pushV[:pushV.index(popV[i]) + 1])
            pushV = pushV[pushV.index(popV[i]) + 1:]
            stack.pop()
        if not stack:
            return True
        return False





def main():
    a = Solution()
    res = a.IsPopOrder([1,2,3,4,5],[4,3,5,1,2])
    print(res)


if __name__ == '__main__':
    main()
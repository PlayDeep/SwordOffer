# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        res = [i for i in range(n)]
        index = 0
        count = 1
        while(len(res)>1):
            if count == m:
                print index
                print res.pop(index)
                if index == len(res):
                    index = 0
                count = 1
                continue
            count += 1
            index += 1
            if index == len(res):
                index = 0
        return res[0]


def main():
    a = Solution()
    res = a.LastRemaining_Solution(5, 3)
    print("res:",res)


if __name__ == '__main__':
    main()
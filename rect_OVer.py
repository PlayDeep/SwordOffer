# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if not number:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        res = [0,1,2]
        for i in range(3, number + 1):
            res.append(res[i-1] + res[i-2])
        print res
        return res[-1]

def main():
    a = Solution()
    res = a.rectCover(5)
    print(res)


if __name__ == '__main__':
    main()
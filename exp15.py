# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        while(n):
            n = (n - 1) & n
            count +=1
        return count
    def func(self,n):
        i = 1
        count = 0
        while():
            if n&i:
                count += 1
            i = i << 1
            print i
        return count


def main():
    a = Solution()
    res = a.NumberOf1(15)
    res = a.func(10)
    print(res)


if __name__ == '__main__':
    main()
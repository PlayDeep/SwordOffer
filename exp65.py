# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while(num2!=0):
            nsum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = nsum
            num2 = carry
        return num1



def main():
    a = Solution()
    res = a.Add(10, 3)
    print("res:",res)


if __name__ == '__main__':
    main()
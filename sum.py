# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        return int(n <= 1 or n + self.Sum_Solution(n - 1))


def main():
    a = Solution()
    res = a.Sum_Solution(1)
    print(res)


if __name__ == '__main__':
    main()
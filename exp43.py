# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 考虑排列组合中，1的个数
        if n <= 0 and isinstance(n, int):
            return 0
        numbers = str(n)
        return self.number_of_1(numbers)

    def number_of_1(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1 and nums[0] == '0':
            return 0
        if length == 1 and nums[0] > '0':
            return 1
        num_first_digit = 0
        if nums[0] > '1':
            num_first_digit = self.PowerBase10(length - 1)
        elif nums[0] == '1':
            num_first_digit = int(nums[1:]) + 1
        num_other_digit = int(nums[0]) * (length - 1) * self.PowerBase10(length - 2)
        num_recursive = self.number_of_1(nums[1:])
        return num_first_digit + num_other_digit + num_recursive

    def PowerBase10(self, n):
        res = 1
        for i in range(n):
            res *= 10
        return res

def main():
    a = Solution()
    res = a.NumberOf1Between1AndN_Solution(10)
    print(res)


if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        start = 0
        end = len(numbers)
        middle = (end - start) / 2
        index = self.parttion(numbers, start, end)
        while (index != middle):
            if index > middle:
                end = index - 1
                index = self.parttion(numbers, start, end)
            else:
                start = index + 1
                index = self.parttion(numbers, start, end)
            print index
        print("nums: {0} \t middle:{1}".format(numbers, middle))
        if self.check_more_than_half(numbers, numbers[middle]):
            return numbers[middle]
        return 0

    def parttion(self, nums, start, end):
        index = start
        for i in range(start + 1, end):
            if nums[index] > nums[i]:# 小于index 放到index前面
                nums.insert(0, nums.pop(i))
                index += 1

        print index, nums
        return index

    def check_more_than_half(self, nums, value):
        n_value = 0
        for i in nums:
            if i == value:
                n_value += 1
        return n_value > len(nums) / 2

class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        save_count = 1
        save_value = numbers[0]
        for i in numbers[1:]:
            if save_count == 0:
                save_count = 1
                save_value = i
            elif i == save_value:
                save_count += 1
            else:
                save_count -= 1

        if save_count > 0 and self.check_more_than_half(numbers, save_value):
            return save_value
        return 0

    def check_more_than_half(self, nums, value):
        n_value = 0
        for i in nums:
            if i == value:
                n_value += 1
        return n_value > len(nums) / 2


def main():
    a = Solution2()
    res = a.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])
    print(res)


if __name__ == '__main__':
    main()
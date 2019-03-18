# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None :
           return None
        xor_res = 0
        for i in array:
            xor_res ^= i
        index_1 = 1
        while(xor_res&1!=0):
            xor_res >> 1
            index_1 += 1
        nums1 = 0
        nums2 = 0
        for i in array:
            if self.is_bit1(i, index_1):
                nums1 ^= i
            else:
                nums2 ^= i
        return [nums1,nums2]


    def is_bit1(self, data, index):
        data = data >> index
        return data & 1



def main():
    a = Solution()
    res = a.FindNumsAppearOnce([1,1,1,1,4,6])
    print(res)


if __name__ == '__main__':
    main()
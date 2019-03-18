# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        single = []
        double = []
        for i in range(len(array)):
            if array[i] % 2 != 0:
                single.append(array[i])
            else:
                double.append(array[i])
        return single + double



def main():
    a = Solution()
    res = a.reOrderArray([2,3,4,6,7,8])
    print(res)


if __name__ == '__main__':
    main()
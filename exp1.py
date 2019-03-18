# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or target is None:
            return 0
        while len(array) > 0 and len(array[0]) > 0:
            r_up = array[0][-1]
            if target < r_up:# 删除所在的列
                for i in range(len(array)):
                    array[i].pop()
            elif target > r_up:#删除所在的行
                array.pop(0)
            else:
                return True
        return False


def main():
    a = Solution()
    res = a.Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
    print(res)

if __name__ == '__main__':
    main()
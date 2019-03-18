# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        arr = rotateArray
        length = len(arr)
        mid = length // 2
        if length == 0 :
            return 0
        if arr[0] >= arr[-1]:
            if length == 2:
                return arr[mid]
            if arr[mid] >= arr[0]:
                return self.minNumberInRotateArray(arr[mid:])
            elif arr[mid] <= arr[-1]:
                return self.minNumberInRotateArray(arr[:mid+1])
        return arr[mid]

def main():
    a = Solution()
    res = a.minNumberInRotateArray([4,3])
    print(res)

if __name__ == '__main__':
    main()
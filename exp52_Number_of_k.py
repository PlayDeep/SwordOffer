# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data or not k:
            return 0
        length = len(data)
        a = self.get_last_k(data, k, 0, length)
        if a != -1:
            b = self.get_first_k(data, k, 0 , length)
        else:
            return 0
        print a, b
        return a - b + 1

    def get_first_k(self, data, k, start, end):
        mid = (start + end) / 2
        if data[mid] == k:
            if mid > 0 and data[mid - 1] == k:
                return self.get_first_k(data, k, start, mid -1)
            else:
                return mid
        elif data[mid] > k:
            return self.get_first_k(data, k, start, mid-1)
        elif mid + 1 <= end:
            return self.get_first_k(data, k, mid+1, end)
        return -1

    def get_last_k(self, data, k, start, end):
        mid = (start + end) / 2
        if data[mid] == k:
            if mid < end - 1 and data[mid + 1] == k:
                return self.get_last_k(data, k, mid+1, end)
            else:
                return mid
        elif data[mid] > k:
            return self.get_last_k(data, k, start, mid-1)
        elif mid + 1 < end:
            return self.get_last_k(data, k, mid+1, end)
        return -1

def main():
    a = Solution()
    res = a.GetNumberOfK([1,2,3,3,3,3],3)
    print(res)


if __name__ == '__main__':
    main()
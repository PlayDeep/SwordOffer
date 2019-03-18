# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput) < k:
            return []
        start = 0
        end = len(tinput)
        index = self.partition(tinput, start, end)
        while (index != k):
            if index < k:
                start = index + 1
                index = self.partition(tinput, start, end)
            else:
                end = index
                index = self.partition(tinput, start, end)
        res = tinput[:index]
        return sorted(res)

    def partition(self, nums, start, end):
        index = start
        for i in range(start + 1, end):
            if nums[index] > nums[i]:  # 小于index 放到index前面
                nums.insert(0, nums.pop(i))
                index += 1
        print index, nums
        return index

# -*- coding:utf-8 -*-
class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput) < k:
            return []
        return sorted(tinput)[:k]

# -*- coding:utf-8 -*-
class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput) < k or not k:
            return []
        res = []
        for i in tinput:
            if not res:
                res.append(i)
            elif len(res) < k:
                if i < res[0]:
                    res.insert(0,i)
                elif i >= res[-1]:
                    res.append(i)
                else:
                    for j in range(len(res)):
                        if res[j] > i:
                            break
                    res.insert(j, i)
            elif len(res) == k and i < res[-1]:
                print res
                if i < res[0]:
                    res.insert(0, i)
                    res.pop()
                else:
                    for j in range(len(res)):
                        if res[j] > i:
                            break
                    print j, i, res

                    res.insert(j, i)
                    res.pop()
        return res




def main():
    a = Solution3()
    res = a.GetLeastNumbers_Solution([4,5,1,6,2,7,2,8],2)
    print(res)


if __name__ == '__main__':
    main()
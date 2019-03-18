class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        ugly_nums = [None for _ in range(index)]
        ugly_nums[0] = 1
        next_ugly_id = 1

        p_multiply2 = 0
        p_multiply3 = 0
        p_multiply5 = 0

        while(next_ugly_id < index):
            min_n = self.min(ugly_nums[p_multiply2]*2, ugly_nums[p_multiply3]*3, ugly_nums[p_multiply5]*5)
            ugly_nums[next_ugly_id] = min_n

            while(ugly_nums[p_multiply2] * 2 <= ugly_nums[next_ugly_id]):
                p_multiply2+=1
            while (ugly_nums[p_multiply3] * 3 <= ugly_nums[next_ugly_id]):
                p_multiply3+=1
            while (ugly_nums[p_multiply5] * 5 <= ugly_nums[next_ugly_id]):
                p_multiply5+=1

            next_ugly_id +=1
        print ugly_nums

        return ugly_nums[next_ugly_id - 1]

    def min(self, a, b, c):
        return min([a,b,c])

def main():
    a = Solution()
    res = a.GetUglyNumber_Solution(14)
    print(res)


if __name__ == '__main__':
    main()
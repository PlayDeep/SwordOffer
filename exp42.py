class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return array
        path = [array[0]]
        max_path = [array[0]]
        max_sum = array[0]
        cur_sum = array[0]
        for i in array[1:]:
            if cur_sum < 0:
                path = []
                cur_sum = 0
            path.append(i)
            cur_sum += i
            if max_sum < cur_sum:
                max_sum = cur_sum
                max_path = path
        print(max_path)
        return max_sum


def main():
    a = Solution()
    res = a.FindGreatestSumOfSubArray([2,8,1,5,9])
    print(res)


if __name__ == '__main__':
    main()
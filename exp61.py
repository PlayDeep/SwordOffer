class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return 0
        numbers.sort()
        num0 = 1 if numbers[0]==0 else 0
        for i in range(len(numbers[1:])):
            if numbers[i] == 0:
                num0 += 1
            elif numbers[i] - numbers[i-1] == 1:
                continue
            elif numbers[i] - numbers[i-1] == num0:
                num0 = 0
                continue
            else:
                return False
        return True


def main():
    a = Solution()
    res = a.IsContinuous([0,3,2,6,4])
    print(res)


if __name__ == '__main__':
    main()
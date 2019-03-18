# -*- coding:utf-8 -*-

class Solution:
    def check(self, i, j, threshold):
        return sum(map(int,str(i)+str(j))) < threshold

    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <=0 or cols <= 0:
            return 0

        class Context:
            acc = 0

        def moving_func(i, j, matrix):
            matrix[i][j] = 0
            Context.acc += 1
            if i - 1 >= 0 and matrix[i-1][j] and self.check(i-1, j, threshold):
                moving_func(i-1, j, matrix)

            if i + 1 < rows and matrix[i+1][j] and self.check(i +1, j, threshold):
                moving_func(i+1, j, matrix)

            if j-1>=0 and matrix[i][j-1] and self.check(i, j -1, threshold):
                moving_func(i, j-1, matrix)

            if j+1<cols and matrix[i][j+1] and self.check(i, j+1, threshold):
                moving_func(i, j+1, matrix)
            return


        matrix = [[1 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if self.check(i, j, threshold):
                    moving_func(i, j, matrix)
                    return Context.acc


def main():
    a = Solution()
    res = a.movingCount(15,20,20)
    print(res)


if __name__ == '__main__':
    main()
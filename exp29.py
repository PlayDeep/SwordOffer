#encoding=utf-8
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        print rows, cols
        start = 0
        res = []
        while (rows > start * 2 and cols > start * 2):
            self.print_matrix_in_circle(matrix, rows, cols, start, res)
            start += 1
        return res

    def print_matrix_in_circle(self, matrix, rows, cols, start, res):
        col = cols - start - 1
        row = rows - start - 1
        for i in range(start, col+1): #
            res.append(matrix[start][i])
        if start < row:
            for i in range(start + 1, row + 1): #
                res.append(matrix[i][col])
        if row > start and col > start:
            for i in range(col-1, start-1, -1):
                res.append(matrix[row][i])
        if col > start and start < row - 1:
            for i in range(row-1, start, -1):
                res.append(matrix[i][start])

        return res


def main():
    a = Solution()
    res = a.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(res)


if __name__ == '__main__':
    main()
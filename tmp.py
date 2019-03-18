# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True

        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols + j] = '0'
        if i < rows-1 and matrix[(i+1) * rows +j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i + 1, j)
        elif i > 0 and matrix[(i-1) * rows + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i - 1, j)
        elif j < cols-1 and matrix[i*cols + j +1 ] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1)
        elif j > 0 and matrix[i*cols + j -1 ] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)
        else:
            return False



def main():
    a = Solution()
    res = a.hasPath("ABCESFCSADEE",3,4,"ABCCED")
    print(res)


if __name__ == '__main__':
    main()
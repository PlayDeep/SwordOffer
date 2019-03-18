# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A or len(A) < 2:
            return A
        length = len(A)
        B = []
        C = [1 for _ in A]
        D = [1 for _ in A]
        C[0] = A[0]
        for i in range(1,length):
            C[i] = C[i-1] * A[i-1]
        for i in range(length-2, -1,-1):
            D[i] = D[i+1] * A[i+1]
        for i in range(length):
            B.append(C[i] * D[i])
        print C, D
        return B

# -*- coding:utf-8 -*-
class Solution2:
    def multiply(self, A):
        if not A or len(A) < 2:
            return A
        length = len(A)
        B = []
        arr = [1]
        for i in A[:-1]:
            arr.append(i*arr[-1])
        arr2 = arr
        arr2.append(1)
        arr2.pop(0)
        print arr, arr2
        for i in range(length):
            B.append(arr[i] * arr2[i])
        return B


def main():
    a = Solution2()
    res = a.multiply([1,2,3,4,5])
    print("res:",res)


if __name__ == '__main__':
    main()
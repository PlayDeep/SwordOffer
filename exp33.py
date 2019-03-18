# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence or len(sequence)==1:
            return True
        min_seq = []
        max_seq = []
        flag = True
        for i in sequence[:-1]:
            if i > sequence[-1]:
                max_seq.append(i)
                flag = False
            elif flag:
                min_seq.append(i)
            else:
                return False
        if not min_seq:
            return self.VerifySquenceOfBST(max_seq)
        if not max_seq:
            return self.VerifySquenceOfBST(min_seq)
        return self.VerifySquenceOfBST(min_seq) and self.VerifySquenceOfBST(max_seq)



def main():
    a = Solution()
    res = a.VerifySquenceOfBST([4,6,7,5])
    print(res)


if __name__ == '__main__':
    main()
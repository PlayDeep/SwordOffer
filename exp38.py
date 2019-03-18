import copy
class Solution:
    res = []

    def Permutation(self, ss):
        self.recursion_permutation(list(ss), 0)
        return [i for i in list(set(self.res)) if len(i)==len(ss)]


    def recursion_permutation(self, ss, begin):
        self.res.append(''.join(ss))
        if not ss or len(ss) <= begin:
            return
        for i in range(begin, len(ss)):
            tmp = ss[begin]
            ss[begin] = ss[i]
            ss[i] = tmp
            self.recursion_permutation(ss, begin+1)

            tmp = ss[begin]
            ss[begin] = ss[i]
            ss[i] = tmp

        return

import itertools
class Solution2:
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []
        lst = list(itertools.permutations(list(ss),len(ss)))
        print lst
        for i in range(len(lst)):
            lst[i] = ''.join(lst[i])
        l = list(set(lst))
        return (sorted(l))

def main():
    a = Solution()
    res = a.Permutation('')
    print(res)


if __name__ == '__main__':
    main()
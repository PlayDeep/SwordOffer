# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        count = dict()
        index = dict()
        for i in range(len(s)):
            if s[i] in count.keys():
                count[s[i]] += 1
            else:
                index[i] = s[i]
                count[s[i]] = 1
        print index
        for k, v in index.items():
            if count[v] == 1:
                return k
        return -1

def main():
    a = Solution()
    res = a.FirstNotRepeatingChar('google')
    print(res)


if __name__ == '__main__':
    main()
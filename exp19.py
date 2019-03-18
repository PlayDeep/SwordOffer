# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern)==0:
            return False
        if len(pattern) > 1 and pattern[1] =='*':
            return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # if len(s)>0 and (s[0] == pattern[0] or pattern[0] == '.'):
            #     return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # else:# 尽管和上面的有重叠，但是不能省略， 因为如果不匹配，就没有其它or了
            #     return self.match(s, pattern[2:])
        if len(s)>0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.match(s[1:], pattern[1:])
        return False

def main():
    a = Solution()
    res = a.match("","b*a")
    print(res)


if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
class Solution:
    def max_length_norepeat_str(self, strs):
        if not strs:
            return ''
        cur_strs = ''
        max_strs = ''
        for i in strs:
            if cur_strs.find(i) > -1:
                index1 = cur_strs.find(i)
                cur_strs = cur_strs[index1+1:] + i
            else:
                cur_strs += i
            if len(cur_strs) >= len(max_strs):
                max_strs = cur_strs
        return max_strs



def main():
    a = Solution()
    res = a.max_length_norepeat_str('arabcacfr')
    print(res)


if __name__ == '__main__':
    main()
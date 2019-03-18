# -*- coding:utf-8 -*-


import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print int(lines[0]) + int(lines[1])
except:
    pass

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.count = []
        self.s = ''

    def FirstAppearingOnce(self):
        return '#' if len(self.count) < 1 else self.count[0]
        # write code here
    def Insert(self, char):
        if char in self.s:
            self.count.remove(char)
        else:
            self.count.append(char)
        self.s += char


def main():
    a = Solution()
    res = a.FirstAppearingOnce()
    print res


if __name__ == '__main__':
    main()


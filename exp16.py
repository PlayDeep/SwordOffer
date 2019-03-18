# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # print "bfujdabjfkd"
        if exponent == 0 or base == 0:
            return 1
        if exponent < 0:
            return 1 / self.Power(base, -1 * exponent)
        if exponent % 2 == 1:
            return base * self.Power(base, exponent - 1)
        return self.Power(base, exponent / 2) * self.Power(base, exponent / 2)

    def Power2(self, base, exponent):
        print("fnaknfkdnaf")
        if exponent == 0 or base == 0:
            return 1
        if exponent < 0:
            return 1 / self.Power2(base, -1 * exponent)
        if exponent % 2 == 1:
            return base * self.Power2(base, exponent - 1)
        res = [0, 1, base, base * base]
        for i in range(2, exponent, 2):
            if i % 2 == 0:
                mid = i / 2
                a = i - mid
                b = mid
                res[i] = res[a] * res[b]
            else:
                mid = (i-1) / 2
                a = (i-1) - mid
                b = mid
                res[i] = res[a] * res[b] * base
        print("exponent{0} res{1}".format(exponent, res[exponent+1]))
        return res[exponent+1]





def main():
    a = Solution()
    res = a.Power2(2,3)
    print(res)


if __name__ == '__main__':
    main()
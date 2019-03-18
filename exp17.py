# -*- coding:utf-8 -*-
class Solution:
    def print_1_to_n(self, n):
        if n <= 0:
            return n
        number = [0] * n
        while(self.is_increment(number)):
            i = 0
            while(not number[i]):
                i+=1
            print(''.join(map(str, number[i:])))


    def is_increment(self, number):
        is_overflow = False
        for i in range(-1, -len(number)-1,-1):
            if is_overflow:
                if i == -len(number) and number[0]==9:
                    return False
                elif number[i] < 9:
                    number[i] += 1
                    return True
                else:
                    number[i] = 0
            elif number[i] == 9:
                is_overflow = True
                number[i] = 0
            else:
                number[i] += 1
                return True

class Solution2:
    def print_1_to_n(self, n):
        if n <=0:
            return
        number = [0 for _ in range(n)]
        for i in range(10):
            number[0] = i
            self.print_1_n_recursive(number, n, 0)

    def print_1_n_recursive(self, number, n, index):
        if index == n-1:
            self.print_number(number)
            return
        for i in range(10):
            number[index+1] = i
            self.print_1_n_recursive(number, n, index+1)

    def print_number(self, number):
        i = 0
        while (len(number) > i and not number[i]):
            i += 1
        print(''.join(map(str, number[i:])))



def main():
    a = Solution2()
    res = a.print_1_to_n(2)
    print(res)


if __name__ == '__main__':
    main()
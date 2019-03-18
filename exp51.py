# -*- coding:utf-8 -*-

class Solution2:
    def InversePairs(self, data):
        if not data or len(data) < 1:
            return 0
        sort_data = sorted(data)
        count = 0
        for i in sort_data:
            index = data.index(i)
            count += index
            data.pop(index)
        return count % 1000000007

class Solution:
    def InversePairs(self, data):
        if not data or len(data) < 1:
            return 0
        count = self.func(data[:], data[:], 0, len(data) - 1)
        print "data", data
        return count%1000000007


    def func(self, data, tmp, start, end):
        if end - start < 1:
            return 0
        mid = (end + start) // 2
        print 'before', data, tmp, data == tmp
        cnt = self.func(tmp, data, start, mid) + self.func(tmp, data, mid+1, end) #为什么data和tmp在此处需要交叉一下？
        print 'after', data, tmp, data == tmp
        i = start
        j = mid+1
        id = start
        while(i<= mid and j <= end):
            if data[i] > data[j]:
                tmp[id] = data[j]
                cnt += mid - i + 1
                j +=1
            else:
                tmp[id] = data[i]
                i += 1
            id += 1

        while(i<=mid):
            tmp[id] = data[i]
            id +=1
            i += 1

        while(j<=end):
            tmp[id] = data[j]
            id += 1
            j += 1

        return cnt

    def inverse_pair(self,data, tmp, start, end):
        if end - start < 1:
            return 0
        mid = (start + end) // 2
        print 'before', data, tmp, data == tmp
        cnt = self.inverse_pair(tmp, data, start, mid) + self.inverse_pair(tmp, data, mid + 1, end)
        print 'after', data, tmp, data==tmp
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start

        while (i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while (i <= mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while (j <= end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt



# -*- coding:utf-8 -*-
class Solution2:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data) - 1, data[:]) % 1000000007

    def inverseCount(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid + 1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start

        while (i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while (i <= mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while (j <= end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt


def main():
    a = Solution2()
    res = a.InversePairs([1,2,3,4,5,6,7,0])
    print(res)


if __name__ == '__main__':
    main()
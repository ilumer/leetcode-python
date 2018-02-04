# coding:utf-8


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # s = ''
        # count = 1
        # while(len(s) < n):
        #     s += str(count)
        #     count += 1
        # return int(s[n-1])
        # 这个方法的时间复杂度偏高　需要加快增长的速度
        len, count, start = 1, 9, 1
        while(n > len * count):
            n -= len*count
            len += 1
            count *= 10
            start *= 10
        # 判断n数所处的区间
        start = start - 1
        if n % len == 0:
            number, digit = start + n // len, -1
        else:
            number, digit = start + n // len + 1,  n % len - 1
        # 寻找对应的数和相对应的位置
        return int(str(number)[digit])

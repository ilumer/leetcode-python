# coding: utf-8


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while(i < n):
            n = n - i
            i = i + 1
        return i if n == i else i - 1
    # 同时这个可以使用二分法　(1 + 2 + .....+ x=n) =>(x+1)x/2=n

# coding:utf-8
class Solution(object):
    def guessNumber(self, n):
        """
        : type n:int
        : rtype: int
        """
        low, high = 0, n
        while(low <= high):
            mid = low + int((high - low)/2)
            state = guess(mid)  # guess 是预定义的函数
            if state == 0:
                return mid
            elif state == 1:  # guess number is lower
                low = mid + 1
            else:  # guess number is higher
                high = mid - 1
        return low
    #  使用二分法

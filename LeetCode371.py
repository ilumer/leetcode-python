# -*- coding: utf-8 -*-

class Solution(object):
    def getSum(self,a,b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        while(b!=0):
            sum = a ^ b
            carry = (a& b) << 1
            a ,b = sum,carry
            #python 会出现超过0x7FFFFFF http://www.lightxue.com/python-integer-overflow
            #https://ych0112xzz.github.io/2016/10/27/OperationwithBits/
        
        return a

    
    #https://leetcode.com/problems/sum-of-two-integers/discuss/84282
    """def getSum(self, a, b):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask) 得到超出32bit表示范围的数，取反可以得到负数
    """


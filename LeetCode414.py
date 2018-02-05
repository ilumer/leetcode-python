# coding: utf-8
import sys


class solution(object):
    def thirdMax(self, nums):
        """
        :type: nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        first, second, third = [-0x80000000] * 3
        for x in nums:
            # 不能重复的数字
            if x not in [first, second, third]:
                if x > first:
                    third, second, first = second, first, x
                elif x > second:
                    third, second = second, x
                elif x > third:
                    third = x
        return third if third != -0x80000000 else first

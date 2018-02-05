# coding: utf-8


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = [0 for i in range(0, 58)]
        # 26*2 + 6
        for x in s:
            index = ord(x) - ord('A')
            # print(x, index)
            letter[index] = letter[index] + 1
        sum = 0
        for i in letter:
            if i % 2 == 0:
                sum += i
            else:
                sum += i - 1
        return sum + 1 if len(s) > sum else sum

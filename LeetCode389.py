# coding:utf-8


class Solution(object):
    def findTheDifference(self, s, t):
        """
        : type s: str
        : type t: str
        : rtype: str
        """
        value, generate_value = 0, 0
        for i in s:
            value += ord(i)
        for j in t:
            generate_value += ord(j)
        return chr(generate_value-value)

        # sum1 = sum(map(ord,list(s)))

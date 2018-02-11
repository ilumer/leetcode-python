# coding: utf-8


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        return len(s.split())
        """
        words = s.split(' ')
        count = 0
        for i in words:
            if i != '':
                count += 1
        return count

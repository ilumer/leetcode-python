# coding:utf-8
import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        list = []
        for i in range(0, 12):
            for x in range(0, 60):
                if (bin(i)+bin(x)).count('1') == num:
                    list.append("{}:".format(i)+str(x).zfill(2))
                    # "%d:%02d" % (i,x)
        return list

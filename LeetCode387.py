# coding:utf-8

# https://leetcode.com/problems/first-unique-character-in-a-string/description/


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for x in s:
            if x not in dict.keys():
                dict[x] = 1
            else:
                value = dict[x]
                dict[x] = value + 1
        list = [x for x, y in dict.items() if y == 1]
        print(list)
        return min(s.index(x) for x in list) if len(list) != 0 else -1

if __name__ == '__main__':
    print(Solution().firstUniqChar(""))

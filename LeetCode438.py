# coding: utf-8


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s:str
        :type p:str
        :rtype: List[int]
        """
        # 窗口移动方法的介绍　https://www.geeksforgeeks.org/window-sliding-technique/
        result = []
        if len(s) < len(p):
            return []
        value = [0, 0]
        p_value = [0, 0]
        for i in range(len(p)):
            value[0] ^= ord(s[i])
            value[1] += ord(s[i])
            p_value[0] ^= ord(p[i])
            p_value[1] += ord(p[i])
        if value[0] ^ p_value[0] == 0 and value[1] == p_value[1]:
            result.append(0)
        # 在窗口移动的方法中出现偶数个相同的字母时,取反的零失效　无法证明是否由相同的字母组成
        # 特殊字符　'af' 与　'be' 在这两个比较的情况下相同
        for i in range(len(p), len(s)):
            value[0] = value[0] ^ ord(s[i-len(p)]) ^ ord(s[i])
            value[1] = value[1] - ord(s[i-len(p)]) + ord(s[i])
            if value[0] ^ p_value[0] == 0 and value[1] == p_value[1]:
                result.append(i-len(p)+1)
        return result

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m:
            return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

    # https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/ 
    # 很好理解的窗口移动　新建的数组作为一个hashmap只要保证对应的hashcode的值相同即可

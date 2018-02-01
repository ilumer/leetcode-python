# coding:utf-8

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # O(mn)
        magazine_list = list(magazine)
        for x in ransomNote:
            if x not in magazine_list:
                return False
            else:
                magazine_list.remove(x)
        return True
    
    #　https://discuss.leetcode.com/topic/53864/java-o-n-solution-easy-to-understand 这是采用了hash的方法　
    # 同时用数组代替了字典

if __name__ == "__main__":
    Solution().canConstruct("aa","ab")
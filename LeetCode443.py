# coding: utf-8


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        compress_char = chars[0]
        for index in range(1, len(compress_char)):
            if ord(compress_char) ^ ord(chars[index]):
                chars[index] = '-1'
            else:
                compress_char = chars[index]
        count = 1
        for c in chars:
            if c != '-1':
                count = 1
            else:
                count +=1
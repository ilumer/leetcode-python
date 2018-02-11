# coding: utf-8


class Solution(object):
    def addString(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype str
        获取每个位置上的值,然后从右到左开始计算。如果最后的进位为１,则加上１。然后反转后输出
        """
        result = []
        digit = 0
        for i in range(0, max(len(num1), len(num2))):
            first_number_value = int(num1[-(i+1)]) if i < len(num1) else 0
            second_number_value = int(num2[-(i+1)]) if i < len(num2) else 0
            total_value = first_number_value+second_number_value+digit
            digit = 0 if total_value < 10 else 1
            result.append(str(total_value % 10))
        if digit == 1:
            result.append('1')
        return ''.join(reversed(result))

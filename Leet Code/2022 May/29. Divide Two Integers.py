class Solution:
    def divide(self, dividend, divisor):
        result = 0
        negativeStatus = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                result += 1 << i
        if negativeStatus:
            result *= -1
        return min(max(-2147483648, result), 2147483647)
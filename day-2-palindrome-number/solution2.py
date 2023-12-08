# This solution doesn't convert to a string
# it's very crude, but seems efficient compared to string operations
# it makes use of integer division and modulus

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative numbers aren't palindromes
        if x < 0: return False

        # single digit numbers are palindromes
        if x < 10: return True

        r_val = 10
        # allows us get the left most digit of the right value value after
        r_val_counter = 1
        # using this value because we know that our max int (2^31 - 1) is 10 digits
        l_val = 1000000000
        # allows us get the right most digit of the left value value after
        l_val_counter = 10

        while x // l_val == 0:
            l_val //= 10

        while l_val >= r_val:
            # Fail fast
            if x // l_val % l_val_counter != x % r_val // r_val_counter:
                return False
            l_val //= 10
            r_val *= 10
            r_val_counter *= 10

        return True

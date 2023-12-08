class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        x_str = str(x)
        ptr1 = 0
        ptr2 = len(x_str) - 1

        while (ptr1 < ptr2):
            if x_str[ptr1] != x_str[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        
        return True

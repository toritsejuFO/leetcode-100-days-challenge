class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        stack = []

        # It's not valid if it's not even in the first place
        if len_s % 2 != 0: return False

        for i in range(len_s):
            len_stack = len(stack)
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif s[i] == ')' and len_stack != 0 and stack[len_stack - 1] == '(':
                stack.pop()
            elif s[i] == '}' and len_stack != 0 and stack[len_stack - 1] == '{':
                stack.pop()
            elif s[i] == ']' and len_stack != 0 and stack[len_stack - 1] == '[':
                stack.pop()
            # Any other situation outside the above if statements will result as invalid
            else: return False

        return True if len(stack) == 0 else False

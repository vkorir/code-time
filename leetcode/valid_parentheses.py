class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack, i = [s[0]], 1
        opening, closing = {'(', '{', '['}, {')', '}', ']'}
        while len(stack) > 0:
            if i == len(s):
                return False
            if s[i] in opening:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                op = stack.pop()
                if s[i] == ')' and op != '(':
                    return False
                if s[i] == '}' and op != '{':
                    return False
                if s[i] == ']' and op != '[':
                    return False
            i += 1
        return True


s = Solution()
print (s.isValid('(]'))
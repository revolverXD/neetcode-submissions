class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        parenthese_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        if s[0] in parenthese_dict:
            return False
        parenthese = []
        for paren in s:
            if paren not in parenthese_dict:
                parenthese.append(paren)
            else:
                if not parenthese:
                    return False
                test = parenthese.pop()
                if test == parenthese_dict[paren]:
                    continue 
                else:
                    return False
        return not parenthese
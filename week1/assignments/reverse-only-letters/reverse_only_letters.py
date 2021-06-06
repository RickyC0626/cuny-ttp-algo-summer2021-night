class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Returns the reversed string, where any character that's not a letter stays in the same place.
        
        constraints:
            no more than 100 characters, could have empty string
            char ASCII codes are between 33 and 122 inclusive
            string does not contain \ or "
            
        example:
            input: s = "abc-d"
            output: "dcb-a"
            
            input: s = "Leet-code!"
            output: "edoc-teeL!"
            
        pseudocode:
        
            def reverseOnlyLetters(s):
                pointer on both ends of string
                iterate through string:
                    if both pointers are letters, swap them
                    otherwise increment/decrement the pointer that is not a letter
        """
        start, end = 0, len(s) - 1
        new_s = list(s)
        
        while start < end:
            if not s[start].isalpha():
                start += 1
            elif not s[end].isalpha():
                end -= 1
            else:
                new_s[start], new_s[end] = new_s[end], new_s[start]
                start += 1
                end -= 1
        
        return ''.join(new_s)
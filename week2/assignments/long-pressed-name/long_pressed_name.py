class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Return True if typed name is a possible outcome of name after
        some keys (or none) are long pressed.

        constraints:
            number of characters in name no less than 1, up to 1000
            number of characters in typed no less than 1, up to 1000
            name and typed contain only lowercase English letters

        examples:
            input: name = "alex", typed = "aaleex"
            output: true
            explanation: 'a' and 'e' in 'alex' were long pressed

            input: name = "saeed", typed = "ssaaedd"
            output: false
            explanation: 'e' must have been pressed twice, but it wasn't in typed output

            input: name = "leelee", typed = "lleeelee"
            output: true

            input: name = "laiden", typed = "laiden"
            output: true
            explanation: it's not necessary to long press any character

        pseudocode:

            def isLongPressedName(name, typed):
                iterate through name:
                    keep 2 pointers on name and typed
                    increment name pointer if char in name is same as typed
                    return False if typed_ptr did not move at all or adjacent typed chars are not equal
                return True

        """
        name_ptr = 0
        for typed_ptr in range(len(typed)):
            if name_ptr < len(name) and name[name_ptr] == typed[typed_ptr]:
                name_ptr += 1
            elif typed_ptr == 0 or typed[typed_ptr] != typed[typed_ptr - 1]:
                return False

        return name_ptr == len(name)
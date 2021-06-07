class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack

        constraints:
            haystack could be empty
            needle could be empty
            haystack and needle contains only lowercase English letters

        clarification:
            return 0 when needle is an empty string

        examples:
            input: haystack = "hello", needle = "ll"
            output: 2

            input: haystack = "aaaaa", needle = "bba"
            output: -1

            input: haystack = "", needle = ""
            output: 0

        pseudocode:

            def strStr(haystack, needle):
                if needle not in haystack:
                    return -1
                if needle == '':
                    return 0

                iterate through string, no greater than length of haystack - needle:
                    check slice of string from index i to i + length of needle
                    return index i if sliced string matches needle

        """
        if needle == '': return 0
        if needle not in haystack: return -1

        # We'll iterate up to the difference of haystack and needle length
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle: return i
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Returns longest common prefix amongst an array of strings,
        or empty string if none.

        constraints:
            no empty arrays
            strings can be empty
            strings only contain lowercase English letters

        examples:
            input: strs = ["flower", "flow", "flight"]
            output: "fl"

            input: strs = ["dog", "racecar", "car"]
            output: ""

        pseudocode:

            def longestCommonPrefix(strs):
                iterate through strings of array:
                    add char to prefix array if all strings have the same letter in common
                    otherwise, break from loop
                return common prefix

        """
        prefix = []

        # Iterate through all strings in parallel by zipping letters at the same index for each string into tuples
        #
        # ('f', 'f', 'f')
        # ('l', 'l', 'l')
        # ('o', 'o', 'i')
        #
        for s in zip(*strs):
            # If the same letters are grouped together from each string, then set length is 1
            # We do this until there is no single common letter in a tuple
            if len(set(s)) == 1:
                prefix.append(s[0])
            else:
                break

        return ''.join(prefix)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Return maximum amount of split balanced strings

        constraints:
            no empty strings
            s[i] contains only 'L' or 'R'
            s is a balanced string

        examples:
            input: s = "RLRRRLLRLL"
            output: 2
            explanation: s can be split into "RL" and "RRRLLRLL"
            - considering only amount of R's and L's
            - order doesn't matter

        pseudocode:

            def balancedStringSplit(s):
                iterate through string:
                    if char is R, increment R counter
                    elif char is L, increment L counter
                    
                    if R and L counters are equal, increment split balanced string counter
                return counter

        """
        # Space complexity -> O(1)

        # Counters for 'L' and 'R' chars
        left_count, right_count = 0, 0
        # Amount of split balanced strings
        count = 0

        # Time complexity -> O(n)
        for char in s:
            if char == 'L':
                left_count += 1
            elif char == 'R':
                right_count += 1

            if left_count == right_count:
                count += 1

        return count
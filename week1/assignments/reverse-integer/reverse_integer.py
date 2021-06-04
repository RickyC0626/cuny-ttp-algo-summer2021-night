class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse 32-bit integer

        returns:
            0 - if reversed integer is outside of 32-bit integer range x
            the reversed integer

        constraints:
            -2^31 <= x <= 2^31 - 1

        example:
            input: x = 123
            output: 321

            input: x = 120
            output: 21

            input: x = 0
            output: 0

        pseudocode:

            def reverse(x):
                get each digit from integer, from right to left
                put digit into new integer from left to right
                return reversed integer

        """
        # Time complexity -> O(n) for 1 layer iteration
        # Space complexity -> O(n) for stack and reverse
        stack = []
        reverse = []
        negative = False

        # Getting individual digits from integer
        # We can convert the int to a string, then iterate through it
        for i, digit in enumerate(str(x)):
            # If digit is negative operator, skip and add to the end
            if digit == "-":
                negative = True
            else:
                stack.append(digit)

        if negative:
            stack.append("-")
            negative = False

        # Pop digits from stack and create new integer
        # Digits will be in reversed order
        for i in enumerate(str(x)):
            reverse.append(stack.pop())

        # Check constraints
        new_x = int(''.join(reverse))
        if abs(new_x) < 2 ** 31 and new_x != 2 ** 32 - 1:
            return new_x
        else:
            return 0
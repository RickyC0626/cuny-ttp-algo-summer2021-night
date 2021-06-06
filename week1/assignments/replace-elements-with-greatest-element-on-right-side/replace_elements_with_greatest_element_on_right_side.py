class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Returns updated array after replacing every element with the greatest element
        among the elements to its right. The last element is replaced with -1.

        constraints:
            no empty arrays
            only positive numbers

        examples:
            input: arr = [17, 18, 5, 4, 6, 1]
            output: [18, 6, 6, 6, 1, -1]

            input: arr = [400]
            output: [-1]

        pseudocode:

            def replaceElements(arr):
                iterate through array in reverse:
                    set max value to arr[i], default is -1
                    next biggest number becomes max value
                return modified array

        """
        # Space complexity -> O(1)
        max_num = -1

        # Time complexity -> O(n)
        for i in range(len(arr) - 1, -1, -1):
            max_num, arr[i] = max(max_num, arr[i]), max_num

        return arr
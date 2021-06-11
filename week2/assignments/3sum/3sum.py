class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return array of triplets [nums[i], nums[j], nums[k]] such that
        the indices are not equal and nums[i] + nums[j] + nums[k] == 0

        constraints:
            array can contain between 0 and 3000 elements
            numbers in array could be negative, zero, or positive
            i, j, k indices cannot be equal
            nums[i] + nums[j] + nums[k] == 0
            no duplicate triplets

        examples:
            input: nums = [-1, 0, 1, 2, -1, -4]
            output: [[-1, -1, 2], [-1, 0, 1]]

            sorted: [-4, -1, -1, 0, 1, 2]

            input: nums = []
            output: []

            input: nums = [0]
            output: []

        pseudocode:

            pointers to keep track of three values? iterate in reverse, starting from last element
            we know for sure that the arrays will have at least 3 elements or more, in multiples of 3

            def threeSum(nums):
                if len(nums) % 3 != 0: return []
                iterate through array:
                    3 pointers to keep track of indices
        """
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Check if nums[i] is above 0, if so break loop
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Define j and k pointers
            j, k = i + 1, len(nums) - 1

            while j < k:
                # int variable to store result of 3sum
                res = sum([nums[i], nums[j], nums[k]])
                if res < 0: j += 1
                elif res > 0: k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    # Handle duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    j += 1
                    k -= 1

        return triplets
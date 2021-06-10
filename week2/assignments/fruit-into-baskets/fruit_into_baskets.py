class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        """
        Return total amount of fruit we can collect in each basket.
        We have two baskets, each capable of carrying any quantity of fruit, but
        each basket should only carry one type of fruit.

        In a row of trees, the i-th tree produces fruit with type tree[i].

        Starting from any tree, repeat the following procedure:
        - Add one piece of fruit from current tree to baskets. If we cannot, stop.
        - Move to next tree to the right of current tree. If there is no tree to the right, stop.

        constraints:
            number of trees in a row no less than 1, up to 40000
            number of fruits per tree can be 0 or more, up to the total number of trees

        examples:
            input: [1, 2, 1]
            output: 3
            explanation: we can collect [1, 2, 1]

            input: [0, 1, 2, 2]
            output: 3
            explanation: we can collect [1, 2, 2]

            input: [1, 2, 3, 2, 2]
            output: 4
            explanation: we can collect [2, 3, 2, 2]

            input: [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
            output: 5
            explanation: we can collect [1, 2, 1, 1, 2]

        pseudocode:
        
            Using sliding window

        """
        count = {}
        i = res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        Return longest word in words that can be built one character at a time by
        other words in words. If there is more than one possible answer, return
        longest word with smallest lexicographical order. If there is no answer,
        return empty string.

        constraints:
            number of words no less than 1, up to 1000
            number of characters per word no less than 1, up to 30
            only lowercase English letters

        examples:
            input: words = ["w", "wo", "wor", "worl", "world"]
            output: "world"
            explanation: "world" can be built one character at a time by "w", "wo", "wor", "worl"

            input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
            sorted: words = ["a", "ap", "app", "appl", "apple", "apply", "banana"]
            output: "apple"
            explanation: Both "apply" and "apple" can be built from other words, but
                "apple" is lexicographically smaller than "apply"

        pseudocode:

            def longestWord(words):
                add words and subparts to set
                sort words in ascending lexicographical order (a to z)
                sort words by length in descending order (largest words first) 
                iterate through words:
                    return first occurrence of word that has subparts in set

        """
        words.sort()

        subparts = set()
        for word in words:
            subparts.add(word)

        words.sort(key=lambda w: -len(w))

        for word in words:
            if self.contains(word, subparts):
                return word
        return ''

    def contains(self, word, subparts):
        temp = ''
        for i in range(len(word)):
            temp += word[i]
            if temp not in subparts:
                return False
        return True
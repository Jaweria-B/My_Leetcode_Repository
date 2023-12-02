class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       
        chars_count = [0] * 26

        for c in chars:
            chars_count[ord(c) - ord('a')] += 1

        total = 0

        for word in words:
            word_count = [0] * 26

            for c in word:
                word_count[ord(c) - ord('a')] += 1

            good = True

            for i in range(26):
                if chars_count[i] < word_count[i]:
                    good = False
                    break

            if good:
                total += len(word)

        return total


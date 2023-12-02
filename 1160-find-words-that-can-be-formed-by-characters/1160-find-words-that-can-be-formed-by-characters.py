class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       
        chars_count = defaultdict(int)

        for c in chars:
            chars_count[ord(c) - ord('a')] += 1

        total = 0

        for word in words:
            word_count = defaultdict(int)

            for c in word:
                word_count[ord(c) - ord('a')] += 1

            good = True

            for c, freq in word_count.items():
                if chars_count[c] < freq:
                    good = False
                    break

            if good:
                total += len(word)

        return total


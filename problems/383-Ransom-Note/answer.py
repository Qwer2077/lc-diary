class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 如果ransomNote长度大于magazine的长度的话，magazine一定拼接不出ransomNote
        if len(ransomNote) > len(magazine):
            return False

        alphabet = [0] * 26

        for c in magazine:
            alphabet[ord(c) - ord("a")] += 1

        for c in ransomNote:
            alphabet[ord(c) - ord("a")] -= 1

            if alphabet[ord(c) - ord("a")] < 0:
                return False

        return True

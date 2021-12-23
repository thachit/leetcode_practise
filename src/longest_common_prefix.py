# Link: https://leetcode.com/problems/longest-common-prefix/
from typing import List

test_cases = [
    {
        'input': ["flower", "flow", "flight"],
        'result': "fl"
    },
    {
        'input': ["dog", "racecar", "car"],
        'result': ""
    },
    {
        'input': ["thach", "thao", "tri"],
        'result': "t"
    }
]


class Solution:
    def __str__(self):
        return f"Executed {__file__}"

    def compare_two_word(self, word1, word2):
        prefix = ""
        stop = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(0, stop):
            if word1[i] == word2[i]:
                prefix = prefix + word1[i]
            else:
                break
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for world in strs[1:]:
            prefix = self.compare_two_word(prefix, world)
        return prefix


def main():
    s = Solution()
    for test_case in test_cases:
        result = s.longestCommonPrefix(test_case['input'])
        if result == test_case['result']:
            print('passed')
        else:
            print('failed')
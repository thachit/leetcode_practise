# Link: https://leetcode.com/problems/roman-to-integer/

test_cases = [
    {
        "input": "III",
        'result': 3
    },
    {
        "input": "LVIII",
        'result': 58
    },
    {
        "input": "MCMXCIV",
        'result': 1994
    },
    {
        "input": "MMXXVI",
        'result': 2026
    }
]

symbol_mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def __str__(self):
        return f"Executed {__file__}"

    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        total = 0
        prev = None
        for i in range(1, len(s) + 1):
            c = s[i-1:i]

            if prev is None or symbol_mapping[c] >= symbol_mapping[prev]:
                total = total + symbol_mapping[c]
            else:
                total = total - symbol_mapping[c]
            prev = c

        return total


def main():
    s = Solution()
    for test_case in test_cases:
        result = s.romanToInt(test_case['input'])
        if result == test_case['result']:
            print('passed ', result)
        else:
            print('failed ', result)
# Link: https://leetcode.com/problems/palindrome-number/
import json

test_cases = [
    {
        'input': 121,
        'result': True
    },
    {
        'input': -121,
        'result': False
    },
    {
        'input': 10,
        'result': False
    },
    {
        'input': -101,
        'result': False
    }
]


class Solution:
    def __str__(self):
        return f"Executed {__file__}"

    @staticmethod
    def isPalindromeSolution(x: int) -> bool:
        return False if x < 0 else x == int(str(x)[0:0:-1])

    @staticmethod
    def isPalindrome(x: int) -> bool:
        user_input = str(x)
        user_input = list(user_input)
        user_input.reverse()
        result = ""
        for item in user_input:
            result = result + item

        if result == str(x):
            return True
        return False


def main():
    s = Solution()
    print(s)
    for test_case in test_cases:
        user_input = test_case.get('input')
        expected_result = test_case.get('result')

        act_result = s.isPalindrome(user_input)

        if act_result == expected_result:
            print(f'==> passed {json.dumps(test_case)}')
        else:
            print(f"==> failed {json.dumps(test_case)}")

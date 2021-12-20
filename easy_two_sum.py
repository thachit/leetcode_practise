# Link: https://leetcode.com/problems/two-sum/
# Test Case
# nums = [2,7,11,15], target = 9
# nums = [3,2,4], target = 6
# nums = [3,3], target = 6

from typing import List

test_cases = [
    {
        'nums': [2,7,11,15],
        'target': 9,
        'result': [0, 1]
    },
    {
        'nums': [3,2,4],
        'target': 6,
        'result': [1,2]
    },
    {
        'nums': [3,3],
        'target': 6,
        'result': [0, 1]
    }
]


class Solution:
    def __str__(self):
        return f"Executed {__file__}"

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            i_index = nums.index(i)
            for j in nums[i_index + 1:]:
                if i + j == target:
                    return [i_index, nums.index(j, i_index+1)]
        return []


def main():
    s = Solution()
    for test_case in test_cases:
        result = s.twoSum(test_case['nums'], test_case['target'])
        if result == test_case['result']:
            print('passed')
        else:
            print('failed')
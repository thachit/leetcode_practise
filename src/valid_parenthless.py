from typing import List
import queue

test_cases = [
    {
        'input': "()",
        'result': True
    },
    {
        'input': "()[]{}",
        'result': True
    },
    {
        'input': "(]",
        'result': False
    },
    {
        'input': "{[]{}()([]{[]})}",
        'result': True
    },
    {
        'input': "{{",
        'result': False
    },
    {
        'input': "]",
        'result': False
    }
]

class Solution:
    def __str__(self):
        return f"Executed {__file__}"

    def isValid2(self, s: str) -> bool:
        q = queue.LifoQueue()
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        open_tags = list(mapping.keys())

        for i in s:
            if i in open_tags:
                q.put(mapping.get(i))
            else:
                item = q.get()
                if not item or i != item:
                    return False

        if q.qsize() > 0:
            return False
        return True


    def isValid1(self, s: str) -> bool:
        arr = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        open_tags = list(mapping.keys())

        for i in s:
            if i in open_tags:
                arr.append(mapping.get(i))
            else:
                if len(arr) == 0 or i != arr[-1:][0]:
                    return False
                del arr[-1:]
        if len(arr) > 0:
            return False

        return True


def main():
    s = Solution()
    for test_case in test_cases:
        result = s.isValid2(test_case['input'])
        if result == test_case['result']:
            print('passed')
        else:
            print('failed')
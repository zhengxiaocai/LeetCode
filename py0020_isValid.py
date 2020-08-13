class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            old = s
            if '()' in s:
                s = s.replace('()', '')
            if '{}' in s:
                s = s.replace('{}', '')
            if '[]' in s:
                s = s.replace('[]', '')
            if old == s:
                break
        return len(s) == 0

    def isValid2(self, s: str) -> bool:
        for i in range(len(s)):
            old = s
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if old == s:
                break
        return len(s) == 0


if __name__ == '__main__':
    print(Solution().isValid2('()') is True)
    print(Solution().isValid2('()[]{}') is True)
    print(Solution().isValid2('(]') is False)
    print(Solution().isValid2('([)]') is False)
    print(Solution().isValid2('{[]}') is True)

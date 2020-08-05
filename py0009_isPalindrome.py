# >>TODO: 字符串反转请用str[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == ''.join(reversed(str(x)))

    def isPalindrome1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome1(121) == True)
    print(Solution().isPalindrome1(-121) == False)
    print(Solution().isPalindrome1(10) == False)

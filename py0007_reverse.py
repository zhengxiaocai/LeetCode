class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(x)[1:][::-1])
        return result if -(2 ** 31) <= result <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    print(Solution().reverse(123) == 321)
    print(Solution().reverse(230) == 32)
    print(Solution().reverse(-23) == -32)
    print(Solution().reverse(-230) == -32)
    print(Solution().reverse(1534236469) == 0)

    print(''.join(list(reversed('123'))))

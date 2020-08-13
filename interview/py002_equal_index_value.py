"""
 问题：有一个有序整数数组A[0…n-1]，数组中的每个元素各不相同。
 编写一个方法，在数组中找出一个索引i，使得A[i] == i。如果存在，返回索引i；
 如果不存在，返回-1。
 -22 -14 1 3 5 7 8 9 11 12
 0   1   2 3 4 5 6 7 8  9
"""


def solution(l):
    for index, value in enumerate(l):
        if index > value:
            return -1
        if index == value:
            return index
    return -1


if __name__ == '__main__':
    list01 = [-22, -14, 1, 3, 5, 7, 8, 9, 11, 12]
    list02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list03 = [2, 3, 4, 5]
    print(solution(list01))
    print(solution(list02))
    print(solution(list03))

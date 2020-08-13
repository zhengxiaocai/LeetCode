# 问题：s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"


def solution(l):
    return ''.join(sorted(set(l)))


if __name__ == '__main__':
    s = 'ajldjlajfdljfddd'
    print(solution(s))

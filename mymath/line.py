"""1-1 함수 플로터: 두 점을 지나는 직선 y = ax + b."""


def slope(p1, p2):
    """두 점 p1 = (x1, y1), p2 = (x2, y2)를 지나는 직선의 기울기 a를 돌려준다.

    x1 == x2이면 세로선이라 함수가 아니므로 ValueError를 낸다.
    """
    raise NotImplementedError


def line_through(p1, p2):
    """두 점을 지나는 직선 y = ax + b의 (a, b)를 돌려준다."""
    raise NotImplementedError

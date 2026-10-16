"""1-1 함수 플로터: 두 점을 지나는 직선 y = ax + b. 기댓값은 numpy로 계산한다."""

import numpy as np
import pytest

from mymath.line import line_through, slope

POINT_PAIRS = [
    ((1000, 150), (3000, 350)),  # 오늘의 센서
    ((0, 1), (2, 5)),
    ((-3, 4), (1, -4)),  # 내려가는 직선
    ((2, 7), (5, 7)),  # 가로선: 기울기 0
]


@pytest.mark.parametrize("p1, p2", POINT_PAIRS)
def test_line_through_matches_numpy(p1, p2):
    expected_a, expected_b = np.polyfit([p1[0], p2[0]], [p1[1], p2[1]], 1)
    a, b = line_through(p1, p2)
    assert a == pytest.approx(expected_a)
    assert b == pytest.approx(expected_b)


def test_slope_of_sensor():
    assert slope((1000, 150), (3000, 350)) == pytest.approx(0.1)


def test_point_order_does_not_matter():
    forward = line_through((1000, 150), (3000, 350))
    backward = line_through((3000, 350), (1000, 150))
    assert backward == pytest.approx(forward)


def test_vertical_line_is_not_a_function():
    with pytest.raises(ValueError):
        slope((2, 1), (2, 5))

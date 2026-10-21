"""1-2 확률 시뮬레이터: 독립인 서버를 직렬로 이었을 때의 가동률. 기댓값은 numpy로 계산한다."""

import numpy as np
import pytest

from mymath.prob import series_availability, simulate_series

CASES = [
    [0.99] * 5,  # 오늘의 서비스
    [0.99] * 100,
    [0.9, 0.95, 0.5],
    [1.0, 0.8],  # 절대 안 죽는 서버가 끼어 있으면?
]


@pytest.mark.parametrize("ps", CASES)
def test_series_availability_matches_numpy(ps):
    assert series_availability(ps) == pytest.approx(np.prod(ps))


@pytest.mark.parametrize("bad", [1.2, -0.1])
def test_probability_must_be_between_0_and_1(bad):
    with pytest.raises(ValueError):
        series_availability([0.99, bad])


def test_simulation_is_close_to_formula():
    ps = [0.99] * 5
    assert simulate_series(ps, n=200_000, seed=0) == pytest.approx(np.prod(ps), abs=0.005)


def test_same_seed_gives_same_result():
    first = simulate_series([0.9, 0.8], n=1000, seed=42)
    second = simulate_series([0.9, 0.8], n=1000, seed=42)
    assert first == second

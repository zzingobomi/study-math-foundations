"""1-2 확률 시뮬레이터: 독립인 서버를 직렬로 이었을 때의 가동률."""

import numpy as np


def series_availability(ps):
    """가동률이 ps인 서버들을 직렬로 이었을 때 서비스 가동률을 돌려준다.

    서버끼리 독립이라고 가정한다. 확률이 0~1 밖이면 ValueError를 낸다.
    """
    a = 1.0
    for p in ps:
        if not 0 <= p <= 1:
            raise ValueError(f'확률은 0~1 사이여야 한다: {p}')
        a *= p        
    return a
    


def simulate_series(ps, n, seed=0):
    """n분 동안 시뮬레이션해서, 모든 서버가 살아 있던 비율을 돌려준다.

    난수는 np.random.default_rng(seed)로 만든다. 씨앗이 같으면 결과도 같다.
    """
    rng = np.random.default_rng(seed)
    up = 0
    for _ in range(n):
        if all(rng.random() < p for p in ps):
            up += 1
    return up / n




        


    

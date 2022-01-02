def solution(n, lost, reserve):
    reserve_ = set(reserve)-set(lost)
    lost_ = set(lost)-set(reserve)

    for st in lost_.copy():
        if st-1 in reserve_:
            lost_ -= {st}
            reserve_ -= {st-1}
        elif st+1 in reserve_:
            lost_ -= {st}
            reserve_ -= {st+1}

    return n - len(lost_)
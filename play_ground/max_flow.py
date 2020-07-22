class MaxFlow(object):
    def __init__(self):
        self._flow = dict()  # {(u0, v0): f(u0, v0), (u1, v1): f(u1, v1), ...}
        self._adj = dict()  # 
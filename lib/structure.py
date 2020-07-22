
# union-find
class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, v):
        if v == self.parent[v]:
            return v
        else:
            self.parent[v] = self.root(self.parent[v])
            return self.parent[v]
    
    def unite(self, u, v):
        u, v = self.root(u), self.root(v)
        if u != v:
            self.parent[u] = v

class SegmentTree(object):
    '''セグメント木
    '''
    def __init__(self, source, operation=min, padding=float('inf')):
        '''2のべき乗の長さのtreeに対し外側をpaddingで埋める
        '''
        self.num = 2**(len(source)-1).bit_length()
        self.padding = padding
        self.operation = operation
        self.tree = [self.padding] * (self.num*2)
        for i in range(len(source)):
            self.tree[self.num+i-1] = source[i]
        for i in range(self.num-2, -1, -1):
            self.tree[i] = self.operation(self.tree[2*i+1], self.tree[2*i+2])

    def get_range(self, a, b):
        a += self.num - 1
        b += self.num - 2
        res = self.padding
        while b-a > 1:
            if a&1 == 0:
                res = self.operation(res, self.tree[a])
            if b&1 == 1:
                res = self.operation(res, self.tree[b])
                b -= 1
            a = a//2
            b = (b-1)//2
        if a == b:
            res = self.operation(res, self.tree[a])
        else:
            res = self.operation(self.operation(res, self.tree[a]), self.tree[b])
        return res
    
    def update(self, a, v):
        raise NotImplementedError


# スライド最小値
def slide_filtering(a, w):
    '''スライドフィルタリング操作のインデックスを返却
    '''
    from collections import deque
    q = deque()
    ret = []
    l, r = 0, 0
    n = len(a)
    for r in range(w):
        while q and a[q[-1]] >= a[r]:
            _ = q.pop()
        q.append(r)
    ret.append(a[q[0]])
    for r in range(w, n):
        while q and a[q[-1]] >= a[r]:
            _ = q.pop()
        q.append(r)
        if q[0] == l:
            _ = q.popleft()
        l += 1
        ret.append(a[q[0]])
    return ret


class FenwickTree(object):
    def __init__(self, n):
        self._bit = [0] * (n+1)
        self.n = n+1
    
    def add(self, i, a):
        i += 1
        while i < self.n:
            self._bit[i] += a
            i += i & -i
    
    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self._bit[i]
            i -= i & -i
        return ret


if __name__ == "__main__":
    a = [-9,5,3,8,-1,5,9,2,4,0,-5,4,6,-8]
    # st = SegmentTree(a)
    # print(st.get_range(2,5))
    # print(st.get_range(5,9))
    # print(st.get_range(0,13))
    # print(st.get_range(1,14))
    # print(st.get_range(0,14))
    # aslide = slide_filtering(a, 4)
    # print(aslide)
    ft = FenwickTree(5)
    ft.add(1,1)
    print(*[ft.sum(i) for i in range(5)])
    ft.add(4,10)
    print(*[ft.sum(i) for i in range(5)])
    ft.add(2,100)
    print(*[ft.sum(i) for i in range(5)])
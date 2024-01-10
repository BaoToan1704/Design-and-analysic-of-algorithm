import math
    
def EuclideanDistance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def BruteForceClosestPair(P):
    n = len(P)
    best = EuclideanDistance(P[0], P[1])
    for i in range(n-1):
        for j in range(i+1, n):
            d = EuclideanDistance(P[i], P[j])
            if d < best:
                best = d
                pair = (P[i], P[j])
    return (best, pair)

def StripClosestPair(P, Q, d):
    mid = len(P) // 2
    xmid = P[mid].x
    S = []
    for point in Q:
        if abs(point.x - xmid) < d:
            S.append(point)
    best = d
    n = len(S)
    for i in range(n-1):
        k = i + 1
        while k <= n-1 and S[k].y - S[i].y < best:
            d = EuclideanDistance(S[i], S[k])
            if d < best:
                best = d
                pair = (S[i], S[k])
            k += 1
    return (best, pair)
    
def EfficientClosestPair(P, Q):
    n = len(P)
    if n <= 3:
        return BruteForceClosestPair(P)
    else:
        mid = n // 2
        Qleft = []
        Qright = []
        for point in Q:
            if point in P[:mid]:
                Qleft.append(point)
            else:
                Qright.append(point)
        (dleft, pairleft) = EfficientClosestPair(P[:mid], Qleft)
        (dright, pairright) = EfficientClosestPair(P[mid:], Qright)
        if dleft < dright:
            d = dleft
            pair = pairleft
        else:
            d = dright
            pair = pairright
        (dstrip, pairstrip) = StripClosestPair(P, Q, d)
        if dstrip < d:
            d = dstrip
            pair = pairstrip
        return (d, pair)
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
# Driver code
P = [Point(2,3), Point(12,30), Point(40,50), Point(5,1), Point(12,10), Point(3,4)]
Q = [Point(2,3), Point(3,4), Point(5,1), Point(12,10), Point(12,30), Point(40,50)]
print(EfficientClosestPair(P, Q))

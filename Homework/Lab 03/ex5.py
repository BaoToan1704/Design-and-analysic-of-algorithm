class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
def convex_hull(points, n):
    if n < 3:
        return
    # Find the leftmost point
    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x:
            l = i
    # Start from leftmost point, keep moving counterclockwise until reach the start point again
    p = l
    q = 0
    while True:
        # Search for a point 'q' such that orientation(p, i, q) is counterclockwise for all points 'i'
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        # Add q to result as a next point of p in the convex hull
        print(points[q])
        # Now q is a previous point of p, so set p as q for next iteration, so that q is added to result
        p = q
        # While we don't come to first point
        if p == l:
            break
        
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0 # colinear
    elif val > 0:
        return 1 # clockwise
    else:
        return 2 # counterclockwise
    
if __name__ == "__main__":
    points = [point(0, 3), point(2, 2), point(1, 1), point(2, 1), point(3, 0), point(0, 0), point(3, 3)]
    convex_hull(points, len(points))

# Basic OP: assignment in line 23
# Worst case: when all the points are on the hull 
# Time complexity: O(n*h) where h is the number of points on the hull
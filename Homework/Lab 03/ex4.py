class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

        
def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def closest_pair(points):
    min_dist = float("inf")
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                p1 = points[i]
                p2 = points[j]
    return p1, p2, min_dist

if __name__ == "__main__":
    points = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4), Point(5, 5)]
    p1, p2, min_dist = closest_pair(points)
    print("The closest pair is {} and {}, with distance {}".format(p1, p2, min_dist))
    


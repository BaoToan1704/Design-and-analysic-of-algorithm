def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    return selected

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print(activity_selection(activities))

# Basic OP: addition in line 6
# Worst case: O(n log n) + O(n) = O(n log n)
# T(n)  = T(n/2) + O(n) = O(n log n)
# Time complexity: O(n log n)
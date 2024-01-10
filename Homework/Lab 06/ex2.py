def job_sequencing(tasks):
    # Sort the tasks in decreasing order of their profits
    tasks.sort(key=lambda x: x[2], reverse=True)
    # Get the maximum deadline
    max_deadline = max(tasks, key=lambda x: x[1])[1]
    # Create a list of free slots
    free_slots = [True] * max_deadline
    # Create a list to store the scheduled tasks
    scheduled_tasks = [None] * max_deadline
    # Iterate through the tasks
    for task in tasks:
        # Find the latest free slot for the task
        for i in range(task[1] - 1, -1, -1):
            if free_slots[i]:
                # Schedule the task
                scheduled_tasks[i] = task
                # Mark the slot as occupied
                free_slots[i] = False
                break
    # Return the list of scheduled tasks
    return scheduled_tasks

if __name__ == "__main__":
    tasks = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25), (6, 2, 20), (7, 5, 8), (8, 7, 10), (9, 4, 12), (10, 3, 5)]
    print(job_sequencing(tasks))
    
# Basic OP: Comparision in line 16
# Worst case: O(n^2)
# T(n)  = T(n-1) + O(n) = O(n^2)
# Time complexity: O(n^2)
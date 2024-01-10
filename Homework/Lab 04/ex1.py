# Find an element in an ascending sorted array. If the element is found, return the index of the element in the array, otherwise, return -1.

def find_element( array, element ):
    if len(array) == 0:
        return -1
    else:
        mid = len(array) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return find_element( array[:mid], element )
        else:
            return find_element( array[mid+1:], element )

if __name__ == '__main__':
    print(find_element([1,2,3,4,5,6,7,8,9], 5))
    print(find_element([1,2,3,4,5,6,7,8,9], 10))

# Basic OP: commparision in line 9
# Worst case: O(log n)
# T(n) = T(n/2) + 1
# Time complexity: O(log n)

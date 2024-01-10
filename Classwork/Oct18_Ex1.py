# Given two sorted arrays, merge them into a sorted array

def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c+=[a[i]]
            i += 1
        else:
            c+=[b[j]]
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]
    print (merge(a, b))
def ex1():
    X = 0
    n = int(input("Enter n: "))
    for i in range(2, n+1):
        X += 1/(1-i**i)
    print("X = ", X)
    
def ex2():
    X = 0
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    for i in range(1, n+1):
        X += (-1)**(i+1) * 1/(m**i)
    print("X = ", X)
    
def ex3():
    Z = 0
    n = int(input("Enter n: "))
    for i in range(n+1):
        Z += i**3
    print("Z = ", Z)

def ex4():
    n = int(input("Enter n: "))
    f = 1
    for i in range(1, n+1):
        f *= i
    print("n! = ", f)

def ex5(n):
    if n == 0:
        return 1
    return n*ex5(n-1)

def ex6():
    # check whether all elements in an array are distinct.
    n = int(input("Enter n: "))
    a = []
    for i in range(n):
        a.append(int(input("Enter a number: ")))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                print("Not distinct")
                return  
    print("Distinct")


def ex7(a, n):
    if n == 0:
        return a[0]
    return max(a[n], ex7(a, n-1))

def ex8():
    n = int(input("Enter n: "))
    a = []
    for i in range(n):
        a.append(int(input("Enter a number: ")))
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    print("Max = ", max)

def ex9(a, n, x):
    if n == 0:
        return False
    if a[n] == x:
        return True
    return ex9(a, n-1, x)

def ex10(a, n, x):
    if n == 0:
        return False
    if a[n] == x:
        return True
    if a[n] < x:
        return False
    return ex10(a, n-1, x)

def ex11():
    n = int(input("Enter n: "))
    a = []
    for i in range(n):
        a.append(int(input("Enter a number: ")))
    x = int(input("Enter x: "))
    for i in range(n):
        if a[i] == x:
            print("Found")
            return
        if a[i] > x:
            print("Not found")
            return
    print("Not found")

def ex12():
    n = int(input("Enter n: "))
    a = []
    b = []
    c = []
    for i in range(n):
        a.append([])
        b.append([])
        c.append([])
        for j in range(n):
            a[i].append(int(input("Enter a number: ")))
            b[i].append(int(input("Enter a number: ")))
            c[i].append(0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end = " ")
        print()

def ex13():
    n = int(input("Enter n: "))
    a = []
    b = []
    for i in range(n):
        a.append([])
        b.append([])
        for j in range(n):
            a[i].append(int(input("Enter a number: ")))
            b[i].append(0)
    x = int(input("Enter x: "))
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j] * x
    for i in range(n):
        for j in range(n):
            print(b[i][j], end = " ")
        print()
        
def ex14():
    n = int(input("Enter n: "))
    a = []
    b = []
    c = []
    for i in range(n):
        a.append([])
        b.append([])
        c.append([])
        for j in range(n):
            a[i].append(int(input("Enter a number: ")))
            b[i].append(int(input("Enter a number: ")))
            c[i].append(0)
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end = " ")
        print()

def ex15():
    n = int(input("Enter n: "))
    a = []
    b = []
    c = []
    for i in range(n):
        a.append([])
        b.append([])
        c.append([])
        for j in range(n):
            a[i].append(int(input("Enter a number: ")))
            b[i].append(int(input("Enter a number: ")))
            c[i].append(0)
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end = " ")
        print()
                
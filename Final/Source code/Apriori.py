import time
"""
The Apiori algorithm
input: D: a set of transactions database, minsup: a user-specified threshold
output: the set of frequent itemsets
Scan the database to calculate the support of all items in I;
F1 = {i|i ∈ I ∧ sup({i}) ≥ minisup }; // F1 : frequent 1-itemsets
k = 2;
while Fk = ∅ do
    Ck = CandidateGeneration (Fk - 1) ; // Ck : candidate k-itemsets
    Remove each candidate X ∈ Ck that contains a (k - 1)-itemset that is not in Fk-1;
    Scan the database to calculate the support of each candidate X ∈ Ck;
    Fk = {X|X ∈ Ck ∧ sup(X) ≥ minsup} ; // Fk : frequent k-itemsets
    k = k + 1;
end
return Uk = 1...k Fk;
"""

def Apiori(D, minsup):  # D: a set of transactions database, minsup: a user-specified threshold
    I = set()  # I: a set of items
    for t in D:
        for i in t:
            I.add(i)
    F1 = set()  # F1 : frequent 1-itemsets
    for i in I:
        if sup({i}, D) >= minsup:
            F1.add(frozenset({i}))
    F = [F1]  # F : a set of frequent itemsets
    k = 2
    while len(F[k - 2]) > 0:
        Ck = CandidateGeneration(F[k - 2])  # Ck : candidate k-itemsets
        Fk = set()  # Fk : frequent k-itemsets
        for X in Ck:
            if sup(X, D) >= minsup:
                Fk.add(X)
        F.append(Fk)
        k += 1
    return F

def CandidateGeneration(Fk_1):  # Fk_1 : frequent k-1-itemsets
    Ck = set()
    for i in Fk_1:
        for j in Fk_1:
            if len(i.union(j)) == len(i) + 1:
                Ck.add(i.union(j))
    return Ck

def sup(X, D):  # X: a set of items, D: a set of transactions database
    count = 0
    for t in D:
        if X.issubset(t):
            count += 1
    return count / len(D)

def main():
    D = [{1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}, {1, 2, 3, 5}]
    minsup = 0.4
    start = time.time()
    F = Apiori(D, minsup)
    for i in range(len(F)-1):
        print("Frequent " + str(i + 1) + "-itemsets: " + str(F[i]))
    end = time.time()
    elapsed = (end - start) * 1000
    print("Time taken: %f ms" % elapsed)
    
if __name__ == "__main__":
    main()
    
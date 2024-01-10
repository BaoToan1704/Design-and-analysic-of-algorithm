import time

def Database(input): # Function to read the database
    listOfTIDs = []     
    listOfItems = []
    for i in input:
        trans = []

        for j in i:
            trans.append([j])

            if [j] not in listOfItems:
                listOfItems.append([j])

        listOfTIDs.append(trans)

    return listOfTIDs, listOfItems

def countSup(itemSet, transDB): # Function to count support of an itemset
    count = 0
    for tid in transDB:
        if itemSet in tid:
            count += 1
    return count


def getFrequentItemSets(C, transDB, minsup):  # Function to generate frequent itemsets
    L = [itemSet for itemSet in C if countSup(itemSet, transDB) >= minsup]
    return L

def candidateItemSets(L):  # Function to generate candidate itemsets
    C = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i][:-1] == L[j][:-1]:  
                C.append(sorted(set(L[i]).union(set(L[j]))))
    return C


def getPassC(prevPassC, C): # Function to generate candidate itemsets for passing
    passC = []
    if (C):
        k = len(C[0]) - 1 # last index
    for t in range(len(prevPassC)):
        Ct= []
        for c in C:
            a = c[:-1]
            b = c[:k-1] + c[k:]
            if a in prevPassC[t] and b in prevPassC[t]:
                Ct.append(c)
        if Ct: passC.append(Ct)
    return passC

def aprioriTID(database, minsup):   # Function to generate frequent itemsets
    C_, C = Database(database)
    L = getFrequentItemSets(C, C_, 3)
    res = []
    while(L): 
        res.append(L)
        C = candidateItemSets(L)
        C_= getPassC(C_, C)
        L = getFrequentItemSets(C, C_, minsup)

    return res

def main():
    test_data = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [1, 2, 3, 5]]
    start = time.time()
    frequent_items = aprioriTID(test_data, 2)
    for i in range(len(frequent_items)):
        print('Frequent', f'{i+1}-itemset: {frequent_items[i]}')
    end = time.time()
    elapsed = (end - start) * 1000
    print("Time taken: %f ms" % elapsed)
    
if __name__ == "__main__":
    main()
    
# Time complexity: O(n^2)
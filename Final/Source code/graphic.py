# Draw the graph to compare running time and memory usage of Apriori.py, AprioriTID.py, FP_Growth.py, Eclat.py, and H-Mine.py.

import Apriori
import AprioriTID
import Eclat
import FP_Growth
import HMine
import time
import numpy as np
import pylab
import tracemalloc

def running_time():
    # Generate a list of random transactions
    transactions = []
    for i in range(100):
        transaction = []
        for j in range(100):
            if np.random.randint(0, 100) < 40:
                transaction.append(j)
        transactions.append(transaction)
        
    # Run Apriori.py
    start = time.time()
    Apriori.main()
    end = time.time()
    apriori_time = end - start
    
    # Run AprioriTID.py
    start = time.time()
    AprioriTID.main()
    end = time.time()
    apriori_tid_time = end - start
    
    # Run FP_Growth.py
    start = time.time()
    FP_Growth.main()
    end = time.time()
    fp_growth_time = end - start

    # Run Eclat.py
    start = time.time()
    Eclat.main()
    end = time.time()
    eclat_time = end - start
    
    # Run H-Mine.py
    start = time.time()
    HMine.main()
    end = time.time()
    hmine_time = end - start

    # Draw the graph
    x = np.arange(5)
    y = [apriori_time, apriori_tid_time, fp_growth_time, eclat_time, hmine_time]
    pylab.bar(x, y, align='center')
    pylab.xticks(x, ('Apriori', 'AprioriTID', 'FP_Growth', 'Eclat', 'H-Mine'))
    pylab.ylabel('Running time (seconds)')
    pylab.show()

def memory_usage():
    # Generate a list of random transactions
    transactions = []
    for i in range(100):
        transaction = []
        for j in range(100):
            if np.random.randint(0, 100) < 40:
                transaction.append(j)
        transactions.append(transaction)
        
    # Run Apriori.py
    tracemalloc.start()
    Apriori.main()
    current, peak = tracemalloc.get_traced_memory()
    apriori_memory = peak
    
    # Run AprioriTID.py
    tracemalloc.start()
    AprioriTID.main()
    current, peak = tracemalloc.get_traced_memory()
    apriori_tid_memory = peak
    
    # Run FP_Growth.py
    tracemalloc.start()
    FP_Growth.main()
    current, peak = tracemalloc.get_traced_memory()
    fp_growth_memory = peak

    # Run Eclat.py
    tracemalloc.start()
    Eclat.main()
    current, peak = tracemalloc.get_traced_memory()
    eclat_memory = peak
    
    # Run H-Mine.py
    tracemalloc.start()
    HMine.main()
    current, peak = tracemalloc.get_traced_memory()
    hmine_memory = peak

    # Draw the graph
    x = np.arange(5)
    y = [apriori_memory, apriori_tid_memory, fp_growth_memory, eclat_memory, hmine_memory]
    pylab.bar(x, y, align='center')
    pylab.xticks(x, ('Apriori', 'AprioriTID', 'FP_Growth', 'Eclat', 'H-Mine'))
    pylab.ylabel('Memory usage (bytes)')
    pylab.show()

if __name__ == '__main__':
    running_time()
    memory_usage()




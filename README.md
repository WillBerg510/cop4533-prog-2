# Programming Assignment 2: Greedy Algorithms

#### Will Berg: 39326193
#### Lam Nguyen: 88729415

Instructions: clone repo into an empty working directory, run main.py and enter the name of a data file without extensions
```
cd src
python main.py
Enter name of data file without extension: file1
```

Assume that all input files are in the correct format. A randomly generated input file can be created by running input-generator.py and following the instructions.

## Written Component

### Question 1: Empirical Comparison

All 3 files can be found in the data folder.

| Input File | k  | m   | FIFO | LRU | OPTFF |
|------------|----|-----|------|-----|-------|
| File1      | 10 | 100 | 71   | 71  | 48    |
| File2      | 20 | 100 | 60   | 54  | 38    |
| File3      | 8  | 250 | 198  | 193 | 126   |

OPTFF has the fewest misses for all 3 files.

FIFO is very similar in performance to LRU, although LRU narrowly performs better for File2 and File3.

### Question 2: Bad Sequence for LRU or FIFO

There does exist a sequence for when k = 3 in which OPTFF has strictly fewer misses than LRU or FIFO.

An example would be when k = 3, m = 6, and r = {1, 2, 3, 4, 1, 2}

The misses for each policy are:

| Policy | Misses |
|--------|--------|
| FIFO   | 6      |
| LRU    | 6      |
| OPTFF  | 4      |

OPTFF performs better here because it can look into future elements of the sequence and see that 3 and 4 will not appear again in the sequence when they are first reached, while 1 and 2 are going to appear again. So, OPTFF will not evict 1 and 2 as they do appear again and 3 gets evicted. The other policies will evict 1 and 2 which will cause a miss when they appear again in the sequence.

The data for the example can be found in the q2.in file, with the output in the q2.out file.

### Question 3: Prove OPTFF Is Optimal

- At a given point in the sequence where the algorithms differ, let A be the integer that some arbitrary offline algorithm removes from the cache, and let B be the integer that Belady's algorithm removes from the cache.
- B is chosen as the integer which appears latest in the sequence, so it necessarily appears later than A.
- Since the arbitrary algorithm has removed A, it will not add A to the cache again until it reaches A next. Therefore, it will have a cache miss when it reaches A. When it then reaches B, it may or may not have a cache miss. So, the arbitrary algorithm will have at least one cache miss.
- Since Belady's algorithm keeps A, it will not remove A from the cache until after reaching A. This is because before reaching A, A will never be the latest integer to appear next. When Belady's algorithm reaches A, there will be no cache miss. Then, since B was removed, there will be a cache miss when the algorithm reaches B. Belady's algorithm will have only one cache miss in this exchange.
- Since Belady's algorithm will have only one cache miss while the arbitrary algorithm has at least one cache miss in this exchange, Belady's algorithm is not adding any more cache misses.
- Therefore, Belady's algorithm is the optimal offline algorithm.
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

OPTFF performs better here because it can look into future elements of the sequence and see that 3 and 4 will not appear again in the sequence when they are first reached, while 1 and 2 are. So, OPTFF will not evict 1 and 2 as they do appear again and 3 gets evicted. The other policies will evict 1 and 2 which will cause a miss when they appear again in the sequence.

The data for the example can be found in the q2.in file, with the output in the q2.out file.
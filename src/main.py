file_name = "generated" # Name used for input and output files goes here

def fifo(k: int, m: int, r: list[int]) -> int:
    cache = []
    miss = 0
    for value in r:
        if value not in cache:
            cache.append(value)
            miss += 1
            if len(cache) > k:
                cache.pop(0)

    return miss

def lru(k: int, m: int, r: list[int]) -> int:
    cache = []
    miss = 0
    for value in r:
        if value not in cache:
            cache.append(value)
            miss += 1
            if len(cache) > k:
                cache.pop(0)
        else:
            cache.pop(cache.index(value))
            cache.append(value)

    return miss

def optff(k: int, m: int, r: list[int]) -> int:
    cache = []
    miss = 0

    # First iteration: create a dictionary that pairs each value with a list of its appearances
    appearances = {}
    for i in range(0, m):
        value = r[i]
        if value in appearances:
            appearances[value].append(i)
        else:
            appearances[value] = [i]

    # Second iteration: go through all requests
    for i in range(0, m):
        value = r[i]
        if value not in cache:
            cache.append(value)
            miss += 1
            if len(cache) > k:
                furthest_position = -1
                furthest_index = -1
                for n in range(0, len(cache) - 1):
                    # If a number in the cache will never appear again, it is an optimal pick for removal
                    if len(appearances[cache[n]]) == 0:
                        furthest_index = n
                        break
                    # Otherwise, find the number that appears the latest
                    if appearances[cache[n]][0] > furthest_position:
                        furthest_index = n
                        furthest_position = appearances[cache[n]][0]
                cache.pop(furthest_index)
        # Remove the current appearance from the dictionary
        appearances[value].pop(0)
    
    return miss



if __name__ == "__main__":
    # Open file
    file = open(f"../data/{file_name}.in", "r")

    # Read first line and split into k and m
    line = file.readline()
    line = line.split()
    k = int(line[0])
    m = int(line[1])

    # Read second line and split it into an integer list
    line = file.readline()
    line = line.split()
    r = []

    for i in line:
        r.append(int(i))

    # FIFO
    fifo_result = fifo(k, m, r)

    # LRU
    lru_result = lru(k, m, r)

    # OPTFF
    optff_result = optff(k, m, r)

    file.close()

    file = open(f"../outputs/{file_name}.out", "w")

    file.write(f"FIFO  : {fifo_result}\n")
    file.write(f"LRU   : {lru_result}\n")
    file.write(f"OPTFF : {optff_result}")
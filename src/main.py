
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



if __name__ == "__main__":
    # Open file
    file = open("../data/generated.in", "r")

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
    optff_result = "TODO"

    file.close()
    print("FIFO  : ", fifo_result)
    print("LRU   : ", lru_result)
    print("OPTFF : ", optff_result)
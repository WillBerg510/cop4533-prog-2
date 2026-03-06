import random

k = input("Input k (cache capacity): ")
while (not k.isdigit()) or int(k) < 1:
  k = input("k must be an integer of at least 1.\nInput k (cache capacity): ")
k = int(k)

m = input("Input m (number of requests): ")
while (not m.isdigit()) or int(m) < 0:
  m = input("m must be a non-negative integer.\nInput m (number of requests): ")
m = int(m)

with open("../data/generated.in", "w") as file:
  file.write(f"{k} {m}")
  file.write("\n")
  for i in range(0, m): # Write m random numbers in the range (1, 2k)
    file.write(f"{random.randint(1, 2 * k)}")
    if (i != m - 1):
      file.write(" ")
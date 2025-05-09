import random
import time
import math

def print_lattice(lattice):
    for row in lattice:
        print(' '.join(map(str, row)))
    print()

def neighbor_sum(lattice, x, y):
    n = len(lattice)
    left = lattice[x][(y - 1) % n]
    right = lattice[x][(y + 1) % n]
    up = lattice[(x - 1) % n][y]
    down = lattice[(x + 1) % n][y]
    
    center = lattice[x][y]
    
    return (center * (left + right + up + down))

def total_magnetization(lattice):
    return sum(sum(row) for row in lattice)

def main():
    n = int(input("Enter Lattice Size:\n"))
    random.seed(time.time())

    lattice_random = [[1 for _ in range(n)] for _ in range(n)]

    print("Initial Lattice:")
    print_lattice(lattice_random)
    print(f"Initial Magnetization: {total_magnetization(lattice_random)}\n")

    KT = 1000
    total_steps = 100

    for step in range(1, total_steps + 1):
        ri = random.randint(0, n - 1)
        rj = random.randint(0, n - 1)

        before_flip = -neighbor_sum(lattice_random, ri, rj)
        lattice_random[ri][rj] *= -1  # flip
        after_flip = -neighbor_sum(lattice_random, ri, rj)

        deltaE = after_flip - before_flip
        P = math.exp(-deltaE / KT)

        print(f"Step {step}:")
        print(f"Flipped element at ({ri},{rj})")
        print(f"Energy before flip: {before_flip}")
        print(f"Energy after flip: {after_flip}")
        print(f"deltaE: {deltaE}")
        print(f"Probability P: {P}")

        if P > random.random():
            print("Flip accepted")
        else:
            print("Flip rejected")
            lattice_random[ri][rj] *= -1 

        print(f"Total Magnetization after step {step}: {total_magnetization(lattice_random)}\n")

    print("Final Lattice:")
    print_lattice(lattice_random)
    print(f"Final Magnetization: {total_magnetization(lattice_random)}")

if __name__ == "__main__":
    main()

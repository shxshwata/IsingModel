import random
import time
import math

def print_lattice(lattice):
    for row in lattice:
        print(' '.join(map(str, row)))
    print()

def sum_lattice(lattice):
    return sum(sum(row) for row in lattice)

def main():
    n = int(input("Enter Lattice Size:\n"))
    random.seed(time.time())

    lattice_random = [[1 for _ in range(n)] for _ in range(n)]

    print("Initial Lattice:")
    print_lattice(lattice_random)
    initial_sum = sum_lattice(lattice_random)
    print(f"Initial Sum: {initial_sum}")

    KT = 1000
    total_steps = 100

    for step in range(1, total_steps + 1):
        ri = random.randint(0, n - 1)
        rj = random.randint(0, n - 1)

        before_flip = -sum_lattice(lattice_random)
        lattice_random[ri][rj] *= -1 
        after_flip = -sum_lattice(lattice_random)

        deltaE = abs(after_flip - before_flip)
        P = math.exp(-deltaE / KT)

        print(f"Step {step}:")
        print(f"Flipped element at ({ri},{rj})")
        print(f"Sum before flip: {before_flip}")
        print(f"Sum after flip: {after_flip}")
        print(f"deltaE (absolute): {deltaE}")
        print(f"Probability P: {P}")

        if P > 0.5:
            print("Flip accepted")
        else:
            print("Flip rejected")
            lattice_random[ri][rj] *= -1

        print()

    print("Final Lattice:")
    print_lattice(lattice_random)
    print(f"Final Sum: {sum_lattice(lattice_random)}")

if __name__ == "__main__":
    main()

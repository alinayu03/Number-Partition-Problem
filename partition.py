import sys
import heapq
import random
import math

def main():
    flag = sys.argv[1]
    algorithm_code = int(sys.argv[2])
    input_file = sys.argv[3]
    data = []
    max_iter = 25000

    try:
        with open(input_file, 'r') as file:
            for line in file:
                data.append(int(line))
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    if algorithm_code == 0:
        print(karmarkar_karp(data))
    elif algorithm_code == 1:
        print(repeated_random(data, max_iter))
    elif algorithm_code == 2:
        print(hill_climbing(data, max_iter))
    elif algorithm_code == 3:
        print(simulated_annealing(data, max_iter))
    elif algorithm_code == 11:
        print(prepartitioned_RR(data, max_iter))
    elif algorithm_code == 12:
        print(prepartitioned_HC(data, max_iter))
    elif algorithm_code == 13:
        print(prepartitioned_SA(data, max_iter))

def karmarkar_karp(data):
    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -abs(first - second))

    residue = -heapq.heappop(max_heap)
    return(residue)


def repeated_random(data, max_iter):
    n = len(data)
    best_solution = [random.choice([-1, 1]) for _ in range(n)]
    best_residue = abs(sum(best_solution[i] * data[i] for i in range(n)))

    for _ in range(max_iter):
        solution = [random.choice([-1, 1]) for _ in range(n)]
        residue = abs(sum(solution[i]*data[i] for i in range(n)))
        if residue < best_residue:
            best_solution = solution[:]
            best_residue = residue
    return best_residue

def hill_climbing(data, max_iter):
    n = len(data)
    solution = [random.choice([-1, 1]) for _ in range(n)]
    best_solution = solution[:]
    best_residue = abs(sum(best_solution[i] * data[i] for i in range(n)))

    for _ in range(max_iter):
        i, j = random.sample(range(n), 2)
        if random.random() < 0.5:
            solution[i] = -solution[i]
        else: 
            solution[j] = -solution[j]
        residue = abs(sum(solution[i]*data[i] for i in range(n)))
        if residue < best_residue:
            best_solution = solution[:]
            best_residue = residue
    return best_residue

def T(iter):
        return (10**10) * (0.8**(iter // 300))

def simulated_annealing(data, max_iter):
    n = len(data)
    solution = [random.choice([-1, 1]) for _ in range(n)]
    residue = abs(sum(solution[i]*data[i] for i in range(n)))

    best_solution = solution[:]
    best_residue = abs(sum(best_solution[i] * data[i] for i in range(n)))

    for i in range(max_iter):
        nei_solution = solution[:]
        i, j = random.sample(range(n), 2)
        if random.random() < 0.5:
            nei_solution[i] = -nei_solution[i]
        else: 
            nei_solution[j] = -nei_solution[j]

        nei_residue = abs(sum(nei_solution[i]*data[i] for i in range(n)))

        if nei_residue < residue:
            solution = nei_solution[:]
            residue = nei_residue
        else:
            if random.random() < math.exp((-(nei_residue-residue))/T(i)):
                solution = nei_solution[:]
                residue = nei_residue

        if residue < best_residue:
            best_solution = solution[:]
            best_residue = residue

    return best_residue

def new_sequence(A, P):
    n = len(A)
    A_prime = [0] * (n + 1)
    for j in range(n):
        A_prime[P[j]] += A[j]
    return A_prime[1:]

def prepartitioned_RR(data, max_iter):
    n = len(data)
    best_residue = float('inf')

    for _ in range(max_iter):
        P = [random.randint(1, n) for _ in range(n)]
        A_prime = new_sequence(data, P)
        residue = karmarkar_karp(A_prime)

        if residue < best_residue:
            best_residue = residue
    
    return best_residue

def prepartitioned_HC(data, max_iter):
    n = len(data)
    P = [random.randint(1, n) for _ in range(n)]
    A_prime = new_sequence(data, P)
    best_residue = karmarkar_karp(A_prime)

    for _ in range(max_iter):
        i, j = random.sample(range(n), 2)
        P[i] = j
        A_prime = new_sequence(data, P)
        residue = karmarkar_karp(A_prime)

        if residue < best_residue:
            best_residue = residue

    return best_residue

def prepartitioned_SA(data, max_iter):
    n = len(data)
    P = [random.randint(1, n) for _ in range(n)]
    A_prime = new_sequence(data, P)
    residue = karmarkar_karp(A_prime)
    best_residue = residue

    for _ in range(max_iter):
        i, j = random.sample(range(n), 2)
        P[i] = j
        A_prime = new_sequence(data, P)
        nei_residue = karmarkar_karp(A_prime)

        if nei_residue < residue:
            residue = nei_residue
        else:
            if random.random() < math.exp((-(nei_residue-residue))/T(i)):
                residue = nei_residue
        if residue < best_residue:
            best_residue = residue

    return best_residue

if __name__ == "__main__":
    main()

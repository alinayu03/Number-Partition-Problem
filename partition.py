import sys
import heapq
import random
import math

def main():
    flag = sys.argv[1]
    algorithm_code = int(sys.argv[2])
    input_file = sys.argv[3]
    data = []
    data_prime = []
    max_iter = 25000

    try:
        with open(input_file, 'r') as file:
            for line in file:
                data.append(int(line))
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    if algorithm_code == 0:
        karmarkar_karp(data)
    elif algorithm_code == 1:
        repeated_random(data, max_iter)
    elif algorithm_code == 2:
        hill_climbing(data, max_iter)
    elif algorithm_code == 3:
        simulated_annealing(data, max_iter)
    elif algorithm_code == 11:
        prepartitioned_repeated_random(data_prime, max_iter)
    elif algorithm_code == 12:
        prepartitioned_HC(data, max_iter)
    elif algorithm_code == 13:
        prepartitioned_SA(data, max_iter)

def karmarkar_karp(data):
    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -abs(first - second))

    residue = -heapq.heappop(max_heap)
    print(residue)
    return(residue)


def repeated_random(data, max_iter):
    n = len(data)
    solution = [random.choice([-1, 1]) for _ in range(n)]
    best_solution = solution[:]
    best_residue = abs(sum(best_solution[i] * data[i] for i in range(n)))

    for _ in range(max_iter):
        solution = [random.choice([-1, 1]) for _ in range(n)]
        residue = abs(sum(solution[i]*data[i] for i in range(n)))
        if residue < best_residue:
            best_solution = solution[:]
            best_residue = residue
    print(best_residue)
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
    print(best_residue)
    return best_residue

def simulated_annealing(data, max_iter):
    n = len(data)
    solution = [random.choice([-1, 1]) for _ in range(n)]
    residue = abs(sum(solution[i]*data[i] for i in range(n)))

    best_solution = solution[:]
    best_residue = abs(sum(best_solution[i] * data[i] for i in range(n)))

    def T(iter):
        return (10**10) * (0.8**(iter // 300))

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

    print(best_residue)
    return best_residue

def prepartition(data):
    p_sequence = {} 
    # p_sequence represents a prepartitioning
    n = len(data) 
    # len of data
    sign = [random.choice([-1, 1]) for _ in range(n)]
    # random signs for determing signs of values
    # needed during prepartitioning
    i, j = random.sample(range(1, n + 1), 2)
    # random indices needed for prepartitioning
    for index in range(len(data)):
    # iterating over indices in data
        if index + 1 < len(data):
            # bounds
            p_sequence[data[i[index]]] = data[i[index]]
            p_sequence[data[j[index]]] = data[j[index]]
            # assings value to corresponding index
            # if p_i = p_j (from P = {P_1, p_2,...p_n}), make signs of data_i
            if p_sequence.get(data[i[index]], None) == p_sequence.get(data[j[index]], None):
                # do they have same index
                data[i[index]] *= sign[index % len(sign)]
                data[j[index]] *= sign[index % len(sign)]
                # if so, assign them the same sign,
                # based on the sign, partition
    data_prime = [0] * len(data)
    # list to store partitioned data
    for index in range(len(data)):
        i,j = p_sequence.get(data[index])
        data_prime[i] = data_prime[i] + data[j]
        
    # yay data is partitioned!!!
    return data_prime


def prepartitioned_repeated_random(data_prime, max_iter):
    n = len(data_prime)
    solution = [random.choice([-1, 1]) for _ in range(n)]
    best_solution = solution[:]
    best_residue = abs(sum(best_solution[i] * data_prime[i] for i in range(n)))

    for _ in range(max_iter):
        solution = [random.choice([-1, 1]) for _ in range(n)]
        residue = abs(sum(solution[i]*data_prime[i] for i in range(n)))
        if residue < best_residue:
            best_solution = solution[:]
            best_residue = residue
    print(best_residue)
    return best_residue




def prepartitioned_HC(data, max_iter):
    return

def prepartitioned_SA(data, max_iter):
    return

if __name__ == "__main__":
    main()

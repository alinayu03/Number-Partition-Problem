import sys
import heapq
import random

def main():
    flag = sys.argv[1]
    algorithm_code = int(sys.argv[2])
    input_file = sys.argv[3]
    data = []
    max_iter = 500

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
    elif algorithm_code == 11:
        prepartitioned_RR(data, max_iter)
    elif algorithm_code == 12:
        prepartitioned_HC(data, max_iter)
    elif algorithm_code == 13:
        prepartitioned_SA(data, max_iter)

def karmarkar_karp(data):
    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    print(max_heap)
    
    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -abs(first - second))
        print(max_heap)

    residue = -heapq.heappop(max_heap)
    print(residue)
    return(residue)


def repeated_random(data, max_iter):
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
    print(best_solution)
    return best_solution
        


def hill_climbing(data, max_iter):
    return

def simulated_annealing(data, max_iter):
    return

def prepartitioned_RR(data, max_iter):
    return

def prepartitioned_HC(data, max_iter):
    return

def prepartitioned_SA(data, max_iter):
    return

if __name__ == "__main__":
    main()

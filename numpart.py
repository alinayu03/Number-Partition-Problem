import sys
import heapq
import random

def main():
    flag = sys.argv[1]
    algorithm_code = int(sys.argv[2])
    input_file = sys.argv[3]
    data = []
    max_iter = 50

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

def prepartition(data):
    p_sequence = {} # p_sequence represents a prepartiotinig
                    # elements in data
    sign = [-1, 1]
    for i in range(len(data)):  # iterating over indices
        if i + 1 < len(data):  # dont go beyond bounds
            p_sequence[data[i]] = data[i]
        if p_sequence[data[i]] == p_sequence[data[i+1]]:
            data[i] *= sign[i % len(sign)]
            data[i+1] *= sign[i % len(sign)]
            # make it so they have the same sign
    return data


    

        
    data_prime = [0]*data
    for i in range(1, len(data)):
        data_prime[i] = data_prime[i] + data[i]
  
def repeated_random(data, max_iter):

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

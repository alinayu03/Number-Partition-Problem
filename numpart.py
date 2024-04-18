import sys
import heapq

def main():
    flag = sys.argv[1]
    algorithm_code = int(sys.argv[2])
    input_file = sys.argv[3]
    data = []

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
        repeated_random(data)
    elif algorithm_code == 2:
        hill_climbing(data)
    elif algorithm_code == 11:
        prepartitioned_RR(data)
    elif algorithm_code == 12:
        prepartitioned_HC(data)
    elif algorithm_code == 13:
        prepartitioned_SA(data)

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


def repeated_random(data):
    return

def hill_climbing(data):
    return

def simulated_annealing(data):
    return

def prepartitioned_RR(data):
    return

def prepartitioned_HC(data):
    return

def prepartitioned_SA(data):
    return

if __name__ == "__main__":
    main()

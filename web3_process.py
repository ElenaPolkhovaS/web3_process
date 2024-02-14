import multiprocessing
from multiprocessing import Pool
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list_sync(numbers):
    results = [factorize(num) for num in numbers]
    return results

def factorize_list_parallel(numbers, pool_size=None):
    with Pool(pool_size) as pool:
        results = pool.map(factorize, numbers)
    return results

if __name__ == '__main__':
    numbers_to_factorize = [999, 564, 12, 99, 18, 21, 8, 9, 144, 72, 25, 128, 255, 99999, 10651060]

    start_time = time.time()
    results_sync = factorize_list_sync(numbers_to_factorize)
    end_time = time.time()
    print(f"Synchronous factorize_list_sync: {results_sync}")
    print(f"Time taken (sync): {end_time - start_time:.6f} seconds")

    start_time = time.time()
    num_processes = multiprocessing.cpu_count()
    results_parallel = factorize_list_parallel(numbers_to_factorize, pool_size=num_processes)
    end_time = time.time()
    print(f'Processor cores: {num_processes}')
    print(f"Asynchronous factorize_list_parallel: {results_parallel}")
    print(f"Time taken (parallel): {end_time - start_time:.6f} seconds")

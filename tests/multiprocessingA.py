import multiprocessing

# def worker_function(parameter):
#     print(f"Working on {parameter}")

# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5]
    
#     # Create a pool with 4 worker processes
#     pool = multiprocessing.Pool(processes=50)
    
#     # Use the pool to execute the worker function in parallel
#     pool.map(worker_function, data)
    
#     # Close the pool and join the processes
#     pool.close()
#     pool.join()


def process_chunk(start, end):
    result = []
    for i in range(start, end):
        # Your processing code here
        result.append(i)
    return result


def main():
    num_processes = 18  # Adjust the number of processes as needed
    total_items = 300  # The total number of iterations in the loop
    chunk_size = total_items // num_processes

    pool = multiprocessing.Pool(processes=num_processes)

    # Split the loop into chunks and distribute them to processes
    chunks = [(i, i + chunk_size) for i in range(2, total_items, chunk_size)]
    
    results = pool.starmap(process_chunk, chunks)
    pool.close()
    pool.join()
    print(chunks)
    # Combine the results from all processes
    combined_result = []
    for result in results:
        combined_result.extend(result)

    print(combined_result)

if __name__ == "__main__":
    main()

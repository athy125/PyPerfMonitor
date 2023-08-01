import pyjemalloc
import timeit

class MemoryBenchmark:
    def __init__(self, runs=5, number=1000):
        self.runs = runs
        self.number = number

    def measure_memory_allocation(self, allocation_size):
        def allocate_memory():
            return pyjemalloc.malloc(allocation_size)

        print(f"Running micro-benchmark for jemalloc memory allocation:")
        allocation_time = timeit.timeit(allocate_memory, number=self.number)  # Warm-up
        allocation_time = timeit.timeit(allocate_memory, number=self.number)  # Measure

        avg_time = allocation_time / self.number
        print(f"Memory allocation of {allocation_size} bytes executed in {avg_time:.6f} seconds "
              f"(average over {self.runs} runs).")


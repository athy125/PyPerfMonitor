from pmu_benchmark import PMUBenchmark
from memory_benchmark import MemoryBenchmark
from custom_benchmark import CustomBenchmark

def example_function():
    for i in range(100000):
        _ = i * i

def custom_hash_collision():
    collisions = 0
    hash_set = set()
    for i in range(10000):
        data = str(i).encode()
        hash_value = hashlib.sha256(data).hexdigest()
        if hash_value in hash_set:
            collisions += 1
        hash_set.add(hash_value)

    print(f"Number of hash collisions: {collisions}")

if __name__ == "__main__":
    pmu_benchmark = PMUBenchmark(runs=5, number=1000)
    pmu_events = [
        "cpu/cache-misses/",
        "cpu/branch-misses/",
    ]
    pmu_benchmark.measure_pmu_counters(example_function, events=pmu_events)

    memory_benchmark = MemoryBenchmark(runs=5, number=1000)
    allocation_size = 1024
    memory_benchmark.measure_memory_allocation(allocation_size)

    custom_benchmark = CustomBenchmark(runs=5, number=1000)
    custom_benchmark.measure_custom_counter(custom_hash_collision)


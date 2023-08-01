# PyPerf a Mini-Benchmarking Library

This is a mini-benchmarking library for Python that allows you to measure CPU Performance Monitoring Unit (PMU) counters, jemalloc memory allocations, and custom measurements like the number of hash collisions.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:

```
git clone https://github.com/athy125/PyPerfMonitor.git
cd PyPerfMonitor
```

2. Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

### 1. PMU Counters Benchmarking

The `pmu_benchmark.py` file provides functionality to measure CPU PMU counters using the `perf` library. You can specify the events to measure and the function you want to benchmark.

Example usage:

```python
from pmu_benchmark import PMUBenchmark

def example_function():
    for i in range(100000):
        _ = i * i

if __name__ == "__main__":
    pmu_benchmark = PMUBenchmark(runs=5, number=1000)
    pmu_events = [
        "cpu/cache-misses/",
        "cpu/branch-misses/",
    ]
    pmu_benchmark.measure_pmu_counters(example_function, events=pmu_events)
```

### 2. Jemalloc Memory Allocation Benchmarking

The `memory_benchmark.py` file provides functionality to measure memory allocations using `pyjemalloc`. You can specify the allocation size and the number of runs.

Example usage:

```python
from memory_benchmark import MemoryBenchmark

if __name__ == "__main__":
    memory_benchmark = MemoryBenchmark(runs=5, number=1000)
    allocation_size = 1024
    memory_benchmark.measure_memory_allocation(allocation_size)
```

### 3. Custom Measurement Benchmarking

The `custom_benchmark.py` file allows you to measure custom computations. In this example, we measure the number of hash collisions for a custom function.

Example usage:

```python
from custom_benchmark import CustomBenchmark

def custom_hash_collision():
    collisions = 0
    # Your custom computation here
    # ...

if __name__ == "__main__":
    custom_benchmark = CustomBenchmark(runs=5, number=1000)
    custom_benchmark.measure_custom_counter(custom_hash_collision)
```

## Contributing

If you want to contribute to this project, feel free to create a pull request or submit an issue.

## License

This project is licensed under the [MIT License](LICENSE).

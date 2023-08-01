import hashlib
import timeit

class CustomBenchmark:
    def __init__(self, runs=5, number=1000):
        self.runs = runs
        self.number = number

    def measure_custom_counter(self, func):
        print(f"Running micro-benchmark for custom counter:")
        results = []
        for _ in range(self.runs):
            start = timeit.default_timer()
            func()
            end = timeit.default_timer()
            results.append(end - start)

        avg_time = sum(results) / self.runs
        print(f"Custom measurement executed in {avg_time:.6f} seconds (average over {self.runs} runs).")


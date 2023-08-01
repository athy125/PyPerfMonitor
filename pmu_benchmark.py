import perf

class PMUBenchmark:
    def __init__(self, runs=5, number=1000):
        self.runs = runs
        self.number = number
        self.runner = perf.Runner()

    def measure_pmu_counters(self, func, events):
        print(f"Running micro-benchmark for PMU counters:")
        for event in events:
            try:
                result = self.runner.bench_func(func, event=event)
                print(f"{event}: {result.mean():.2f} {result.get_unit()}")
            except perf.NoData:
                print(f"Unable to access the '{event}' counter on this system.")
            except perf.PerfError as e:
                print(f"Error while accessing '{event}': {e}")
            print()


"""Performance tests for the data collection service."""
import time
import statistics
import requests

BASE_URL = "http://localhost:5000"
ITERATIONS = 50


def measure(method, url, **kwargs):
    """Send N requests and return min/avg/max response times in ms."""
    times = []
    for _ in range(ITERATIONS):
        start = time.perf_counter()
        response = requests.request(method, url, timeout=5, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        times.append(elapsed)
    return response.status_code, min(times), statistics.mean(times), max(times)


def run():
    """Run performance tests against all endpoints."""
    print(f"Performance test — {ITERATIONS} requests per endpoint\n")
    print(f"{'Endpoint':<35} {'Status':>6} {'Min ms':>8} {'Avg ms':>8} {'Max ms':>8}")
    print("-" * 70)

    tests = [
        ("GET",  "/",            {}),
        ("POST", "/patient",     {"json": {"name": "PerfTest"}}),
        ("GET",  "/patients",    {}),
        ("POST", "/experiment",  {"json": {"name": "PerfExp"}}),
        ("GET",  "/experiments", {}),
        ("POST", "/store",       {}),
    ]

    for method, path, kwargs in tests:
        status, mn, avg, mx = measure(method, BASE_URL + path, **kwargs)
        label = f"{method} {path}"
        print(f"{label:<35} {status:>6} {mn:>8.2f} {avg:>8.2f} {mx:>8.2f}")


if __name__ == "__main__":
    run()

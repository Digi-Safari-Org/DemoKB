# TODO: Analyze and fix the race condition in this multi-threaded counter.
# - Use threading.Lock to make increment() atomic.
# - Validate that actual count equals expected after running multiple times.
# - Challenge: Rewrite with concurrent.futures for advanced users.

import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()  # Add a lock to control access

    def increment(self):
        # Thread-safe version using lock
        with self.lock:
            current_value = self.value
            time.sleep(0.001)  # Simulate some work
            self.value = current_value + 1

def run_concurrent_increments(counter_obj, num_threads, increments_per_thread):
    """
    Runs concurrent increments on a shared counter object.
    This function previously had a subtle race condition.
    """
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=lambda: [counter_obj.increment() for _ in range(increments_per_thread)])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return counter_obj.value

# Test the fix
if __name__ == "__main__":
    for _ in range(5):  # Run multiple times to ensure stability
        num_threads = 5
        increments_per_thread = 100
        my_counter = Counter()
        final_count = run_concurrent_increments(my_counter, num_threads, increments_per_thread)
        print(f"Expected count: {num_threads * increments_per_thread}, Actual count: {final_count}")

##  Lab 3.1: Advanced Logical Bug Detection & Fix (Race Conditions in Threads)

###  Objective:
- Detect and fix **subtle concurrency issues** (race conditions) using GitHub Copilot.
- Understand the limitations of non-atomic operations in multi-threaded code.
- Practice generating fixes using **Copilot Chat** and validate them under load.

---

###  Instructions:

####  Part 1: Run the Buggy Code

1. Review the provided `counter.py` file containing a multi-threaded function with a race condition.
```python 
import threading
import time

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # Simulate a non-atomic operation that can lead to race conditions
        current_value = self.value
        time.sleep(0.001) # Simulate some work
        self.value = current_value + 1

def run_concurrent_increments(counter_obj, num_threads, increments_per_thread):
    """
    Runs concurrent increments on a shared counter object.
    This function contains a subtle race condition.
    """
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=lambda: [counter_obj.increment() for _ in range(increments_per_thread)])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return counter_obj.value

# Example usage (will likely show inconsistent results due to the bug)
# if __name__ == "__main__":
#     my_counter = Counter()
#     final_count = run_concurrent_increments(my_counter, 5, 100)
#     print(f"Expected count: {5 * 100}, Actual count: {final_count}")

```
2. Uncomment the `__main__` block.
3. Run the script multiple times (3–5 times).
4. Observe that the **actual count is often less than the expected count**, indicating a bug due to **concurrent access**.

---

####  Part 2: Analyze with Copilot

1. Use **Copilot Chat** to investigate the issue. 
2. Let Copilot guide you toward the solution.

---

####  Part 3: Fix and Validate

1. Apply Copilot's suggestion (e.g., use `threading.Lock`).
2. Refactor the `increment()` method to use a `with self.lock:` block.
3. Re-run the script 3–5 times.
4. Ensure **actual count now always equals expected count** (`num_threads * increments_per_thread`).

---

####  Challenge Extension (Optional):
Modify the code to:
- Use `concurrent.futures.ThreadPoolExecutor` instead of `threading.Thread`.
- Add an intentional **off-by-one error** and use Copilot to find and fix it.

import csv
import time


def load_ids(path=r"src/data/customer_ids.csv"):
    ids = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.append(row["CustomerID"])
    return ids


# This works correctly, but it's deliberately slow - O(n^2). It has to check
# every item against every other item, so it can't skip work even once a
# duplicate is found - it finds ALL duplicated IDs, not just whether one exists.
# TO DO: Ask your AI tool to analyze why this is slow, then write a faster
# version below. Do not change what it returns - only how it gets there.
def find_duplicate_ids_slow(items):
    duplicates = set()
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                duplicates.add(items[i])
    return sorted(duplicates)


# TO DO: Write your optimized version here
# Your task: Implement a faster way to find all duplicated IDs that returns
# the exact same sorted list as find_duplicate_ids_slow, for any input
# including an empty list or a single-item list.
def find_duplicate_ids_fast(items):
    raise NotImplementedError("Implement the optimized version here")


def main():
    ids = load_ids()

    # TO DO: Baseline
    # Your task: Time find_duplicate_ids_slow against the full dataset and
    # print how many duplicates were found and the time taken.
    start = time.time()
    result_slow = find_duplicate_ids_slow(ids)
    elapsed_slow = time.time() - start
    print(f"Slow version: {len(result_slow)} duplicate IDs found, time={elapsed_slow:.4f}s")

    # TO DO: Optimized run
    # Your task: Once find_duplicate_ids_fast is implemented, time it the same
    # way and compare. Confirm it returns the exact same list as the slow version.
    # start = time.time()
    # result_fast = find_duplicate_ids_fast(ids)
    # elapsed_fast = time.time() - start
    # print(f"Fast version: {len(result_fast)} duplicate IDs found, time={elapsed_fast:.4f}s")
    # assert result_slow == result_fast, "Fast version returned a different result!"

    # TO DO: Edge case check
    # Your task: Construct an empty list and a single-item list, and confirm
    # both find_duplicate_ids_slow and find_duplicate_ids_fast return the same
    # (empty) result for each.

    print("\n✅ Optimization Run Completed!")


if __name__ == "__main__":
    main()

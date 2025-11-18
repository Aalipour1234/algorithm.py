class Algorithms:
    # Recursive Binary Search
    def recursive_binary_search(self, arr, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return self.recursive_binary_search(arr, target, left, mid - 1)
        else:
            return self.recursive_binary_search(arr, target, mid + 1, right)

    # Iterative Binary Search
    def iterative_binary_search(self, arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    # Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        mid  = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + mid + self.quick_sort(right)

    # Insertion Sort
    def insertion_sort(self, arr):
        arr = arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # Selection Sort
    def selection_sort(self, arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


# ====================
# فراخوانی ها
# ====================
algo = Algorithms()
numbers = [34, 7, 23, 32, 5, 62, 12]

print("initial list:", numbers)

print("Quick Sort:", algo.quick_sort(numbers))
print("Insertion Sort:", algo.insertion_sort(numbers))
print("Selection Sort:", algo.selection_sort(numbers))

sorted_nums = sorted(numbers)
target = 23

print("\n ordered list :", sorted_nums)
print("Recursive Binary Search:", algo.recursive_binary_search(sorted_nums, target, 0, len(sorted_nums) - 1))
print("Iterative Binary Search:", algo.iterative_binary_search(sorted_nums, target))
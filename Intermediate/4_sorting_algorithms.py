def bubble_sort(arr):
    """Implements the Bubble Sort algorithm."""
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Implements the Selection Sort algorithm."""
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Implements the Insertion Sort algorithm."""
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("--- Basic Sorting Algorithms ---")
    print(f"Original list: {unsorted_list}\n")

    # --- Bubble Sort ---
    # Create a copy to not modify the original list
    list_for_bubble = unsorted_list.copy()
    sorted_bubble = bubble_sort(list_for_bubble)
    print(f"Bubble Sort Result:   {sorted_bubble}")

    # --- Selection Sort ---
    list_for_selection = unsorted_list.copy()
    sorted_selection = selection_sort(list_for_selection)
    print(f"Selection Sort Result: {sorted_selection}")

    # --- Insertion Sort ---
    list_for_insertion = unsorted_list.copy()
    sorted_insertion = insertion_sort(list_for_insertion)
    print(f"Insertion Sort Result: {sorted_insertion}")
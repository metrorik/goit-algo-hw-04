import timeit
import random



# Алгоритм злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Алгоритм вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst




##############################################################################################
# Функція для генерації випадкових даних
def generate_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Розміри масивів для тестування
sizes = [100, 1000, 10000]

# Словник для зберігання часу виконання
results = {
    'merge_sort': [],
    'insertion_sort': [],
    'timsort': []
}

for size in sizes:
    data = generate_data(size)
    
    # Замір часу для Merge Sort
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    results['merge_sort'].append(merge_sort_time)
    
    # Замір часу для Insertion Sort
    if size <= 10000:  # Обмежуємо, щоб уникнути довгого виконання
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        results['insertion_sort'].append(insertion_sort_time)
    else:
        results['insertion_sort'].append(None)
    
    # Замір часу для Timsort
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    results['timsort'].append(timsort_time)

# Вивід результатів
for size, merge_time, insertion_time, timsort_time in zip(sizes, results['merge_sort'], results['insertion_sort'], results['timsort']):
    print(f"Array Size: {size}")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    if insertion_time:
        print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    else:
        print("Insertion Sort Time: N/A")
    print(f"Timsort Time: {timsort_time:.6f} seconds")
    print("-" * 40)




# Array Size: 100
# Merge Sort Time: 0.000096 seconds
# Insertion Sort Time: 0.000120 seconds
# Timsort Time: 0.000009 seconds
# ----------------------------------------
# Array Size: 1000
# Merge Sort Time: 0.001079 seconds
# Insertion Sort Time: 0.012910 seconds
# Timsort Time: 0.000087 seconds
# ----------------------------------------
# Array Size: 10000
# Merge Sort Time: 0.015042 seconds
# Insertion Sort Time: 1.355228 seconds
# Timsort Time: 0.000974 seconds

# Timsort - Найефективніший алгоритм серед протестованих.
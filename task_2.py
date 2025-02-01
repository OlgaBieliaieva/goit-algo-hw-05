def binary_search_with_bounds(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = float('inf')  # Початкове значення верхньої межі

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        # Оновлення верхньої межі
        if arr[mid] >= target:
            upper_bound = min(upper_bound, arr[mid])
            right = mid - 1
        else:
            left = mid + 1

    # Перевірка на випадок, якщо верхньої межі не знайдено
    return iterations, (upper_bound if upper_bound != float('inf') else None)

# Приклади тестів
sorted_array = [1.1, 2.5, 3.3, 4.8, 5.9, 7.0, 8.6]

print("Binary search results:")
print("Target 4.5:", binary_search_with_bounds(sorted_array, 4.5))  # Шукане число між 4.8
print("Target 7.0:", binary_search_with_bounds(sorted_array, 7.0))  # Шукане число є в масиві
print("Target 9.0:", binary_search_with_bounds(sorted_array, 9.0))  # Число більше за всі елементи
import timeit
from time import time
import random
from string import ascii_letters

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    # Створення таблиці зсувів
    last_occurrence = {char: -1 for char in set(text)}
    for i in range(m):
        last_occurrence[pattern[i]] = i

    i = m - 1

    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j < 0:
            return i + 1
        i += m - min(j, 1 + last_occurrence.get(text[i], -1))
    return -1

# Алгоритм Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return -1

    # Побудова префікс-функції
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            j = lps[j - 1] if j != 0 else 0
    return -1

# Префікс-функція для КМП
def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            length = lps[length - 1] if length != 0 else 0
            i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    if m == 0:
        return -1

    d = 256
    h = pow(d, m - 1) % prime
    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return -1

# Функція для вимірювання часу пошуку
def measure_time(func, text, pattern):
    start_time = time()
    func(text, pattern)
    return round(time() - start_time, 7)

# Читання текстів із файлів
with open("article1.txt", "r", encoding="utf-8") as file1:
    text1 = file1.read()

with open("article2.txt", "r", encoding="utf-8") as file2:
    text2 = file2.read()

# Підрядки для тестів
existing_substring1 = text1[:30]  # Існуючий підрядок у першому тексті
non_existing_substring1 = ''.join(random.choices(ascii_letters, k=30))

existing_substring2 = text2[:30]  # Існуючий підрядок у другому тексті
non_existing_substring2 = ''.join(random.choices(ascii_letters, k=30))

# Тестування алгоритмів на першому тексті
print("Text 1")
print("Boyer-Moore (existing):", measure_time(boyer_moore, text1, existing_substring1))
print("Boyer-Moore (non-existing):", measure_time(boyer_moore, text1, non_existing_substring1))
print("Rabin-Karp (existing):", measure_time(rabin_karp, text1, existing_substring1))
print("Rabin-Karp (non-existing):", measure_time(rabin_karp, text1, non_existing_substring1))
print("KMP (existing):", measure_time(kmp_search, text1, existing_substring1))
# print("KMP (non-existing):", measure_time(kmp_search, text1, non_existing_substring1))

# Тестування алгоритмів на другому тексті
print("Text 2")
print("Boyer-Moore (existing):", measure_time(boyer_moore, text2, existing_substring2))
print("Boyer-Moore (non-existing):", measure_time(boyer_moore, text2, non_existing_substring2))
print("Rabin-Karp (existing):", measure_time(rabin_karp, text2, existing_substring2))
print("Rabin-Karp (non-existing):", measure_time(rabin_karp, text2, non_existing_substring2))
print("KMP (existing):", measure_time(kmp_search, text2, existing_substring2))
# print("KMP (non-existing):", measure_time(kmp_search, text2, non_existing_substring2))
import multiprocessing


def factorial(n):
    print(f"Обчислення факторіалу для числа {n}...")
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Обчислення факторіалу для числа {n} завершено.")
    return result


if __name__ == "__main__":
    numbers = [10, 12, 14, 16, 18, 20]

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    print(f"Факторіали: {results}")

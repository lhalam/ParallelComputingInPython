import multiprocessing
import time
from random import randint


def process_chunk(data_chunk):
    # Імітація обробки даних
    seconds = randint(1, 5)
    print(f"Обробка даних: {data_chunk} і триватиме {seconds} секунд")
    time.sleep(seconds)
    print(f"Обробка даних завершена: {data_chunk}")
    return sum(data_chunk)


if __name__ == "__main__":
    data = list(range(100))
    chunk_size = 20
    data_chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.map(process_chunk, data_chunks)

    print(f"Результат обробки: {sum(results)}")

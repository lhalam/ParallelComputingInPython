import threading
import time
from random import randint


def process_data():
    print("Початок обробки даних...")
    seconds = randint(1, 5)
    print(f"Обробка даних і триватиме {seconds} секунд")
    time.sleep(5)  # Імітація тривалої операції
    print("Обробка даних завершена.")


print("Основний потік: запуск фонової обробки.")
background_thread = threading.Thread(target=process_data)
background_thread.start()

print("Основний потік: продовжує роботу.")
background_thread.join()
print("Основний потік: фонова обробка завершена.")

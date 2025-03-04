import threading
import requests
import time

urls = ["http://example.com", "http://google.com", "http://python.org"]


def download_url(url):
    print(f"Завантаження {url}")
    response = requests.get(url)
    print(f"Downloaded {url}: {len(response.content)} bytes")


start_time = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Загальний час виконання: {end_time - start_time} секунд")

import asyncio
from random import randint


async def read_file(filename):
    seconds = randint(1, 5)
    print(f"Reading {filename} and Sleeping for {seconds} seconds")
    await asyncio.sleep(seconds)
    with open(filename, "r", encoding="utf-8") as f:
        r = f.read()

    print(f"Finished reading {filename}")
    return r

async def main():
    filenames = ["in\\file1.txt", "in\\file2.txt", "in\\file3.txt"]
    tasks = [read_file(filename) for filename in filenames]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

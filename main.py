import asyncio
import random
import sys
import time
from importlib.metadata import version

# ANSI colors
c = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)


async def make_random(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated make_random({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"make_random({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: make_random({idx}) == {i}" + c[0])
    return i


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main_counter():
    await asyncio.gather(count(), count(), count())


async def main():
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    s = time.perf_counter()

    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

    # asyncio.run(main()) # for use with count()

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

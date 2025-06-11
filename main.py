import asyncio
import random
import sys
import time
from importlib.metadata import version
#
from rich.console import Console
from rich.text import Text

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


async def main_random_color():
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    print(f'rich version: {get_package_version("rich")}')

    s = time.perf_counter()

    random.seed(444)
    r1, r2, r3 = asyncio.run(main_random_color())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

    # asyncio.run(main_random_color()) # for use with count()

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


import asyncio
from time import perf_counter


def time_dec(origin_func):
    """vaqtni hisoblash uchun decorator"""

    async def wrapper(*args, **kwargs):
        t1 = perf_counter()
        val = await origin_func(*args, **kwargs)
        t2 = perf_counter() - t1

        print(f"{origin_func.__name__} ishga tushirish vaqti: {t2:.8f} sekund")
        return val

    return wrapper


@time_dec
async def tub_sonlarni_top(son):
    tub_sonlar = []
    for i in range(2, son + 1):
        tub = True
        for j in range(2, i):
            if i % j == 0:
                tub = False
                break
        if tub:
            tub_sonlar.append(i)
            await asyncio.sleep(0)

    return tub_sonlar


async def main():
    son = int(input("son kiriting: "))
    natija = await tub_sonlarni_top(son)
    print(f"{son} songacha bolgan tub sonlar: {natija}")


if __name__ == "__main__":
    asyncio.run(main())

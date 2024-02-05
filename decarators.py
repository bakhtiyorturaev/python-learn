def time_dec(origin_func):
    """vaqtni hisoblash uchun decarator"""

    def wrapper(*args, **kwargs):
        from time import perf_counter
        val = origin_func(*args, **kwargs)
        t1 = perf_counter()

        print(val)

        t2 = perf_counter() - t1
        print(t2)

    return wrapper

#####


def decarator(origin_func):
    """son 0 bo'lsa xatolik qaytar"""

    def wrapper(*args, **kwargs):
        values = origin_func(*args, **kwargs)
        for i in values:
            if i > 0:
                print(i)
            else:
                print("xatolik")

    return wrapper

@decarator
def ikki_son(son):
    return son


a = ikki_son([0, 0])


def HTTS_tekshir(N):
    if len(str(N)) % 2 != 0 and all(int(x) % 2 != 0 for x in str(N)):
        return "YES"
    else:
        return "NO"


N = int(input("Iltimos, bir son kiriting: "))

result = HTTS_tekshir(N)
print(f"N soni HTTS shartlarini qanoatlantirsa: {result}")

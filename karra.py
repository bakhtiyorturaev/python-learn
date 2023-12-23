with open('karra_jadval.txt', 'w') as fayl:
    for j in range(2, 10):
        for i in range(2, 10):
            s = i * j
            print(f"{i}x{j}={s:2}\t", end='')
            fayl.write(f"{i}x{j}={s:2}\t")
            if i == 9:
                print()
                fayl.write('\n')

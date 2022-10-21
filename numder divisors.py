i = int(input());

while i != 0:
    for num in range(1, int(i / 2) + 1):
        if i % num == 0:
            print('divisors', num)
    break

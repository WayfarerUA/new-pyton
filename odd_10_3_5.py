num = int(input());
while num % 10 != 0:
    if num % 2 > 0 and num % 3 == 0 and num % 5 == 0:
            print('its good number')
            break
    print('please change number')
    exit()
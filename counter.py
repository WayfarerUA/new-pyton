
def counter(amount):
    money = [200, 100, 50, 20, 10, 5, 2]
    num = {}
    for a in money:
        if amount >= a:
            num[a] = amount // a
            amount = amount % a

    print ("Колличество банкнот")
    for key, val in num.items():
        print(f"{key} : {val}")

amount = int(input());
counter(amount)
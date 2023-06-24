def digit_root(num):
    while 9 < num < 10000000:
        sum = 0
        while num != 0:
            sum += num % 10
            num //= 10
        num = sum
    return num




number = 12222
count = 1
while number != 1:
    if number % 2 == 0:
        number //= 2
        print(f'{count}- {number}')
        count += 1
    else:
        number = (3 * number) + 1
        print(f'{count}- {number}')
        count += 1

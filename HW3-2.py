def devider_generator(number):
    cursor = 1
    while cursor <= number:
        if number % cursor == 0:
            yield cursor
        cursor += 1


if __name__ == '__main__':
    for dev in devider_generator(1024):
        print(dev)
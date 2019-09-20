def is_power_of_two(n):
    while n > 1:
        n /= 2
    if n == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_power_of_two(64))
    print(is_power_of_two(623))
    print(is_power_of_two(1024))
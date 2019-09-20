def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(41))
    print(is_prime(12))
def is_beauty(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    if n % digits_sum:
        return False
    else:
        return True


if __name__ == "__main__":
    print(is_beauty(36))
    print(is_beauty(-6353))
    print(is_beauty(-51))

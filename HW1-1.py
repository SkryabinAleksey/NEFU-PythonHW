def get_digit_sum(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    return digits_sum


if __name__ == "__main__":
    print(get_digit_sum(-14578))
    print(get_digit_sum(7123413))
    print(get_digit_sum(-5001))

def cyclic_string_generator(file):
    while True:
        with open(file, "r") as f:
            for line in f:
                yield line.strip()


if __name__ == "__main__":
    lines = cyclic_string_generator("row")
    for i, line in enumerate(lines):
        print(line)
        if i > 100:
            break






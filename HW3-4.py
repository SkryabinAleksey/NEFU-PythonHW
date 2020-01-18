def cyclic_string_generator(file):
    while True:
        with open(file, "r") as f:
            for line in f:
                yield line.strip()


def get_len(file):
    gen_cycle = cyclic_string_generator(file)
    while True:
        for i in gen_cycle:
            yield len(i)


if __name__ == "__main__":
    gen_len = get_len("row")
    for i, l in enumerate(gen_len):
        print(l)
        if i > 100:
            break
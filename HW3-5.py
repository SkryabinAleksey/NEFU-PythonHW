def cyclic_string_generator(file):
    while True:
        with open(file, "r") as f:
            for line in f:
                yield line.strip()


if __name__ == "__main__":
    gen = cyclic_string_generator("NOD19")
    filtered_nod = filter(lambda x: "NOD19" in x, gen)
    for i, line in enumerate(filtered_nod):
        print(line)
        if i > 5:
            break
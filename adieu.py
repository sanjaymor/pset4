import inflect


def main():
    names = get_names()
    print(f"Adieu, adieu, to {format_names(names)}")


def get_names():
    names = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            return names

        names.append(name)


def format_names(names):
    p = inflect.engine()
    return p.join(names)


if __name__ == "__main__":
    main()

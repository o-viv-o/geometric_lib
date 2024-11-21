figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3,
}


def calc(fig, func, size):
    assert fig in figs, (
        "Figure '{}' not recognized. Available figures: {}".format(fig, figs)
    )
    assert func in funcs, (
        "Function '{}' not recognized. Available functions: {}".format(func, funcs)
    )

    result = eval("{}.{}(*{})".format(fig, func, size))
    return result


def main():
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input("Enter figure name, available are {}:\n".format(figs))

    while func not in funcs:
        func = input("Enter function name, available are {}:\n".format(funcs))

    size_length = sizes.get("{}-{}".format(func, fig), 1)
    while len(size) != size_length:
        size = list(
            map(int, input("Input figure sizes separated by space:\n").split())
        )

    res = calc(fig, func, size)
    print(res)


if __name__ == "__main__":
    main()

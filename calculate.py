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
        f"Figure '{fig}' not recognized. Available figures: {figs}"
    )
    assert func in funcs, (
        f"Function '{func}' not recognized. Available functions: {funcs}"
    )

    result = eval(f"{fig}.{func}(*{size})")
    return result


def main():
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    size_length = sizes.get(f"{func}-{fig}", 1)
    while len(size) != size_length:
        size = list(
            map(int, input("Input figure sizes separated by space:\n").split())
        )

    res = calc(fig, func, size)
    print(res)


if __name__ == "__main__":
    main()

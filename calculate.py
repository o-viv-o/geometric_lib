import circle as circle
import square as square
import triangle as triangle


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
    assert fig in figs
    assert func in funcs

    if any(s <= 0 for s in size):
        raise ValueError("Size need to be > 0")

    expected_size = sizes.get(f"{func}-{fig}")
    if len(size) != expected_size:
        raise ValueError(
            "Figure '{}' not recognized. Available figures: {}".format(fig, figs)
        )

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated by space\n"
                ).split(" "),
            )
        )

    calc(fig, func, size)

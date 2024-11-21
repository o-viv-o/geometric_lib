from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter


figs = {
    'circle': {
        'area': circle_area,
        'perimeter': circle_perimeter,
    },
    'square': {
        'area': square_area,
        'perimeter': square_perimeter,
    }
}


def calc(fig, func, size):
    result = figs[fig][func](*size)
    return result

if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    if fig == "circle" or fig == "square":
        while len(size) != sizes.get(f"{func}-{fig}", 1):
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space, 1 for circle and square. Sizes need to be > 0\n"
                    ).split(" "),
                )
            )
    else:
        while len(size) != sizes.get(f"{func}-{fig}", 3):
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space, 1 for circle and square. Sizes need to be > 0\n"
                    ).split(" "),
                )
            )

    res = calc(fig, func, size)
    print(res)

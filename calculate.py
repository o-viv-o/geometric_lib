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
    assert fig in figs, "Invalid figure"
    assert func in figs[fig], "Invalid function"
    assert all(s > 0 for s in size), "All dimensions must be positive"

    result = figs[fig][func](*size)
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(
            f"Enter figure name, available are {list(figs.keys())}:\n"
        )

    while func not in figs[fig]:
        func = input(
            f"Enter function name, available are {list(figs[fig].keys())}:\n"
        )

    expected_size_count = 1 if fig == "circle" else 1
    while len(size) != expected_size_count:
        size = list(
            map(
                int,
                input(
                    f"Input {expected_size_count} size(s) separated by space\n"
                ).split(),
            )
        )

    print(calc(fig, func, size))

import circle
import triangle
import square


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

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":  
    
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input("Enter figure name, available are: " + ", ".join(figs) + ": \n")

    while func not in funcs:
        func = input("Enter function name, available are: " + ", ".join(funcs) + ": \n")

    if fig == "circle" or fig == "square":
        while len(size) != sizes.get(f"{func}-{fig}", 1):
            size_input = input("Input figure sizes separated by space.Sizes need to be > 0\n")
            size = list(map(int, size_input.split(" ")))
    else:
        while len(size) != sizes.get(f"{func}-{fig}", 3):
            size_input = input("Input figure sizes separated by space.Sizes need to be > 0\n")
            size = list(map(int, size_input.split(" ")))

    res = calc(fig, func, size)
    print(res)

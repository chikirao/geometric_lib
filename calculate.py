import circle
import square

figs = ["circle", "square"]
funcs = ["perimeter", "area"]


def calc(fig, func, size):
    """
    Выполняет расчет для выбранной фигуры и функции.

    Аргументы:
    fig -- строка, обозначающая фигуру ('circle' или 'square')
    func -- строка, обозначающая функцию ('perimeter' или 'area')
    size -- список с размерами, необходимыми для расчета

    Возвращает результат расчета.
    """
    if fig not in figs:
        raise ValueError(
            f"Unknown figure: {fig}. Valid options are {figs}."
        )
    if func not in funcs:
        raise ValueError(
            f"Unknown function: {func}. Valid options are {funcs}."
        )

    if fig == "circle":
        if func == "area":
            return circle.area(*size)
        if func == "perimeter":
            return circle.perimeter(*size)
    if fig == "square":
        if func == "area":
            return square.area(*size)
        if func == "perimeter":
            return square.perimeter(*size)


if __name__ == "__main__":
    fig = input(f"Enter figure name (available: {figs}):\n").strip()
    func = input(f"Enter function name (available: {funcs}):\n").strip()
    size_inp_msg = "Enter size(s), separated by spaces:\n"
    size = list(map(float, input(size_inp_msg).split()))

    try:
        result = calc(fig, func, size)
        print(f"The {func} of {fig} is {result}")
    except ValueError as e:
        print(e)

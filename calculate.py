import circle  # noqa: F401
import square  # noqa: F401
# Теперть flake игнорирует импорты,
# так как он не понимал, что они для eval

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
    assert fig in figs
    assert func in funcs

    if fig not in figs:
        raise ValueError(
            f"Unknown figure: {fig}. Valid options are {figs}."
        )
    if func not in funcs:
        raise ValueError(
            f"Unknown function: {func}. Valid options are {funcs}."
        )
    try:
        # Используем eval для вызова функции
        result = eval(f"{fig}.{func}(*{size})")
        return result
    except Exception as e:
        raise ValueError(f"Error during calculation: {e}")


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

from function import Function


if __name__ == '__main__':

    f = Function(lambda x: x**3 + x**2 + 1)

    x = 1
    print(f(x))
    print(f.derivative(x))
    print(f.derivative(x, 2))
from function import Function


if __name__ == '__main__':

    f = Function(lambda x: x**3 + x**2 + 1)

    x = 1
    print(f(x))
    print(f.derivative_at(x))
    print(f.derivative_at(x, 2))

    print('')
    print(f.derivative()(x))
    print(f.derivative(2)(x))

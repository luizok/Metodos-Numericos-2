from exceptions import InvalidModeException, InvalidOrderException


class Function:

    def __init__(self, func):
        self.__func = func

    def __call__(self, x):
        return self.__func(x)

    def derivative(self, x, order=1, dx=10e-7, mode='central'):
        if order <= 0:
            raise InvalidOrderException('Order must be > 0')
        
        if mode not in ['backward', 'forward', 'central']:
            raise InvalidModeException('mode must be backward, forward or central')

        return self.__derivative(x,order=order, dx=dx, mode=mode)
    
    def __derivative(self, _x, curr_order=1, order=1, dx=10.e-7, mode='central'):

        if curr_order <= order:
            f = self
            if mode == 'central':
                dfdx = Function(lambda x: (f(x + dx) - f(x - dx)) / (2 * dx))
            elif mode == 'backward':
                dfdx = Function(lambda x: (f(x) - f(x - dx)) / dx)
            elif mode == 'forward':
                dfdx = Function(lambda x: (f(x + dx) - f(x)) / dx)
            
            return dfdx.__derivative(_x, curr_order+1, order, dx, mode)
        
        return self(_x)


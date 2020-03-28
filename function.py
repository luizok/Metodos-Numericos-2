from exceptions import InvalidModeException, InvalidOrderException


class Function:

    def __init__(self, func):
        self.__func = func

    def __call__(self, x):
        return self.__func(x)

    def __choose_mode(self, dx, mode):

        if mode not in ['backward', 'forward', 'central']:
            raise InvalidModeException('mode must be backward, forward or central')

        f = self
        dfdx = None
        if mode == 'central':
            dfdx = Function(lambda x: (f(x + dx) - f(x - dx)) / (2 * dx))
        elif mode == 'backward':
            dfdx = Function(lambda x: (f(x) - f(x - dx)) / dx)
        elif mode == 'forward':
            dfdx = Function(lambda x: (f(x + dx) - f(x)) / dx)

        return dfdx

    def derivative_at(self, x, order=1, dx=10e-7, mode='central'):
        '''
            Returns the value of the derivative of order <order>
            at <x> with  <dx> difference using <mode> approaching
        '''

        if order <= 0:
            raise InvalidOrderException('Order must be > 0')

        return self.__derivative_at(x, order=order, dx=dx, mode=mode)

    def __derivative_at(self, x, curr_order=1, order=1, dx=10e-7, mode='central'):

        if curr_order <= order:
            dfdx = self.__choose_mode(dx, mode)
            return dfdx.__derivative_at(x, curr_order+1, order, dx, mode)

        return self(x)

    def derivative(self, order=1, dx=10e-7, mode='central'):
        '''
            Returns the derivative function of order <order>
            with  <dx> difference using <mode> approaching
        '''

        if order <= 0:
            raise InvalidOrderException('Order must be > 0')

        return self.__derivative(order=order, dx=dx, mode=mode)

    def __derivative(self, curr_order=1, order=1, dx=10e-7, mode='central'):

        if curr_order <= order:
            dfdx = self.__choose_mode(dx, mode)
            return dfdx.__derivative(curr_order+1, order, dx, mode)

        return self

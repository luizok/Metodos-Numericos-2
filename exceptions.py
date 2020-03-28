class InvalidModeException(Exception):
    ''' Raised when mode is not backward,forward or central '''
    pass

class InvalidOrderException(Exception):
    ''' Raised when derivative order is not > 0 '''
    pass
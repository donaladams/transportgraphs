import os.path
from exceptions import ValueError

class CheckPathIsValid(object):
    """ Decorator for functions that take a single argument that
        should be a valid path. If path is invalid, a ValueError is thrown. """

    def __init__(self, f):
        """ Save function to be decorated """
        self.f = f

    def __call__(self, path):
        """ Checks validity of path and then calls function or raises
            ValueError """
        if not os.path.exists(path):
            raise ValueError("{0} is an invalid path".format(path))
        return self.f(path)

def check_value_is_unicode(func):
    """ Used to decorate methods of the form method(self, value)
        to check that the type of value is unicode. """
    def decorator(self, value):
        if not type(value) is unicode:
            raise ValueError("{0} is not unicode!".format(value))
        return func(self, value)
    return decorator
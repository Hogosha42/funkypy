# funkypy.py

from functools import reduce
from types import FunctionType, LambdaType

__all__ = ['lmap', 'mapi', 'mapcur', 'lsfilter', 'funcomp', 'Data', 'Binded']



def funcomp(*functions) -> LambdaType:
    """Compose a function out of all the arguments given in order."""
    return reduce(lambda f,g:lambda x: f(g(x)), functions[::-1])


#========================================================#
# functional ways to convert or apply functions to lists #
#========================================================#

def lmap(function: FunctionType, ls: list) -> list:
    """Builds a new list whose elements are the results of applying the given function to each of the elements of the list"""
    return list(map(function, ls))

def mapcur(function: FunctionType) -> LambdaType:
    """curried version of lmap, good for uses in pipelines"""
    return lambda x: list(map(function, x))

def mapi(function: FunctionType, ls: list) -> list:
    """Builds a new list whose elements are the results of applying the given function to each of the elements of the list. The function must have two input arguments for the element and the index."""
    return list(map(function, range(len(ls)),ls))

def lsfilter(conditional: FunctionType, ls: list) -> list:
    """Returns a new list containing only the elements of the list for which the given conditional returns 'True'"""
    return [x for x in ls if conditional(x)]



#======================================================#
#  Data class - to easily pipe data through functions  #
#======================================================#

class Data:

    def __init__(self, data):
        self.data = data
    
    def __rshift__(self, other):
        return Data(other(self.data))

    def __repr__(self):
        return str(self.data)

    def val(self):
        return self.data

#======================================================#
#  Bind - to bind functions and easily deal with None  #
#======================================================#


def _bindfun(function: FunctionType):
    return lambda x: function(x) if x != None else x


class Binded():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args , **kwargs):
        return self.func(*args, **kwargs)

    def bind(self):
        return _bindfun(self.func)



if __name__ == "__main__":
    
    @Binded
    def add2(x):
        return x+2

    @Binded
    def add4(x):
        return x+4

    def times2(x):
        return x*2
  
    (Data(None) 
    >> add2.bind()
    >> add4.bind()
    >> print)
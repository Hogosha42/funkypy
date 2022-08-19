from functools import reduce

__all__ = ["lmap", "mapi", "mapcur", "lsfilter", "funcomp", "Data", "Binded"]



def funcomp(*funcs):
    return reduce(lambda f,g:lambda x: f(g(x)), funcs[::-1])


#========================================================#
# functional ways to convert or apply functions to lists #
#========================================================#

def lmap(fun, ls):
    return list(map(fun, ls))

def mapcur(fun):
	return lambda x: list(map(fun, x))

def mapi(fun, ls):
	return list(map(fun, range(len(ls)),ls))

def lsfilter(conditional, ls):
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

    def value(self):
        return self.data

#======================================================#
#  Bind - to bind functions and easily deal with None  #
#======================================================#


def _bindfun(fun):
    return lambda x: fun(x) if x != None else x


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
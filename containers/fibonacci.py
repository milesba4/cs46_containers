
##########################################################################
# example fibonacci number code;
# you do not have to modify this code in any way
##########################################################################


def fibs(n):
    '''
    This function computes the first n fibonacci numbers.
    Notice that this function uses O(n) memory.
    '''
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    '''
    This function computes the n-th fibonacci number,
    but it uses O(n) memory to do so,
    which is bad.
    '''
    return fibs(n)[-1]


def fib(n):
    '''
    This function computes the n-th fibonacci number,
    but it consumes only O(1) memory,
    and is optimal.
    '''
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


##########################################################################
# fibonacci number code using generators;
# you will need to implement the functions below
##########################################################################


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''

    def __init__(self, n=None):
        '''
        n is the number of iterations we will run;
        if n is None, then we will run forever
        '''
        self.n = n

    def __iter__(self):
        '''
        Every class that supports the __iter__ method is an "iterable".
        All iterables support for loops and can be converted into a list.
        '''
        return FibIter(self.n)

    def __repr__(self):
        if self.n is not None:
            return f'Fib({self.n})'
        else:
            return 'Fib()'


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.f0 = 0
        self.f1 = 1

    def __next__(self):
        '''
        Return the "next" factorial number in our sequence.
        The factorial number corresponding to position self.i
        '''
        if self.n is not None:
            if self.i >= self.n:
                # we're at the end of the iteration
                # if we never raise StopIteration,
                # then the loop will go on forever
                raise StopIteration
            elif self.i == 0:
                self.i += 1
                return 1
            else:
                self.f2 = self.f1 + self.f0
                self.f0 = self.f1
                self.f1 = self.f2
                self.i += 1
                return self.f2
        elif self.i == 0:
            self.i += 1
            return 1
        else:
            self.f2 = self.f1 + self.f0
            self.f0 = self.f1
            self.f1 = self.f2
            self.i += 1
            return self.f2


def fib_yield(n=None):
    '''
    This function returns a generator that computes
    the first n fibonacci numbers.
    If n is None, then the generator is infinite.
    '''
    f0 = 1
    f1 = 1
    if n is not None:
        for i in range(n):
            if i < 2:
                yield 1
            else:
                f2 = f1 + f0
                f0 = f1
                f1 = f2
                yield f2
    else:
        yield 1
        yield 1
        while True:
            f2 = f1 + f0
            f0 = f1
            f1 = f2
            yield f2

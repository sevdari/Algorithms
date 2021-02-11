class SqMatrix:
    """
    A suqare matrix class. The internal representation uses a list,
    in row-major order.
    The elements must be numbers.
    Supports the following operations, with the usual mathematical
    interpretation: +, -, @, *.
    """

    def __init__(self, n):
        """
        Creates an n×n matrix filled with zeros.
        """
        if not (isinstance(n, int) and n >= 0):
            raise Exception("n must be a non-negative integer")
        self.n = n
        self.l = [0] * n**2

    def shape(self):
        return (self.n, self.n)

    ## Given the row and column indices (each a number between 0 and n-1)
    ## returns the corresponding index in the internal list.
    ## This is an internal method.
    def _getind(self, row, col, check_args = True):
        if check_args:
            if not (isinstance(row, int) and 0 <= row < self.n):
                raise Exception(f"out of bounds row, should be an int in 0..{self.n-1}")
            if not (isinstance(col, int) and 0 <= col < self.n):
                raise Exception(f"out of bounds col, should be an int in 0..{self.n-1}")
        return row * self.n + col

    ## A string showing the contents of the matrix
    def __repr__(self):
        n = self.n
        s = f"SqMatrix of size {n}x{n}:\n"
        maxchars = max(len(f"{x:g}") for x in self.l)
        # linelen = (maxchars+3) * n + 1
        # horiz_line = '+' + '-' * (linelen-2) + '+\n'
        horiz_line = '+' + ('-' * (maxchars + 2) + '+') * n + '\n'
        s += horiz_line
        for row in range(n):
            s += "| "
            for col in range(n):
                ind = self._getind(row, col, check_args = False)
                x = self.l[ind] # element at position row,col
                # s += f"{x:.2f}".rjust(maxchars) + (" | " if col < n-1 else " |\n")
                s += f"{x:g}".rjust(maxchars) + (" | " if col < n-1 else " |\n")
            s += horiz_line
        # s += horiz_line
        return s

    ## Basic method to define m[row,col]
    ## NOTE: delegates the argument check to _getindex
    ##       (avoid code duplication)
    def __getitem__(self, key):
        row, col = key # unpack the key
        return self.l[self._getind(row, col)]

    ## Basic method to define m[row,col] = v
    ## NOTE: delegates the argument check to _getindex
    ##       (avoid code duplication)
    def __setitem__(self, key, v):
        row, col = key # unpack the key
        self.l[self._getind(row, col)] = v

    def __eq__(self, other):
        if isinstance(other, SqMatrix):
            if self.shape() != other.shape():
                return False
            n = self.n
            for row in range(n):
                for col in range(n):
                    if self[row,col] != other[row,col]:
                        return False
            return True
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, SqMatrix):
            if self.shape() != other.shape():
                raise Exception("other must be a matrix of the same size")
            n = self.n
            ret = SqMatrix(n)
            for row in range(n):
                for col in range(n):
                    ret[row,col] = self[row,col] + other[row,col]
            return ret
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, SqMatrix):
            if self.shape() != other.shape():
                raise Exception("other must be a matrix of the same size")
            n = self.n
            ret = SqMatrix(n)
            for row in range(n):
                for col in range(n):
                    ret[row,col] = self[row,col] - other[row,col]
            return ret
        return NotImplemented

    def __matmul__(self, other):
        if isinstance(other, SqMatrix):
            if self.shape() != other.shape():
                raise Exception("other must be a matrix of the same size")
            n = self.n
            ret = SqMatrix(n)
            for row in range(n):
                for col in range(n):
                    s = 0
                    for k in range(n):
                        s += self[row,k] * other[k,col]
                    ret[row,col] = s
            return ret
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, SqMatrix):
            return self @ other
        if isinstance(other, (int,float)):
            return self._scalarmul(other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def _scalarmul(self, other):
        n = self.n
        ret = SqMatrix(n)
        for row in range(n):
            for col in range(n):
                ret[row, col] = other * self[row, col]
        return ret

    def fill(self, x):
        n = self.n
        for row in range(n):
            for col in range(n):
                self[row, col] = x

    ## A very inefficient implementation! (but short and simple)
    def __pow__(self, k):
        if not (isinstance(k, int) and k >= 0):
            raise Exception("k must be a non-negative int")
        ret = SqMatrix.identity(self.n)
        for i in range(k):
            ret = ret @ self
        return ret

    ## identity matrix of size n
    ## [not a method! an alternative constructor!]
    def identity(n):
        ret = SqMatrix(n)
        for i in range(n):
            ret[i,i] = 1
        return ret

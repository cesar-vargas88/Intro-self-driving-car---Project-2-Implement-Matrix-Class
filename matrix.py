import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        
        det = 0
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        elif self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        # TODO - your code here
        elif self.h == 1:
            det = self.g[0][0]
        else:
            det = self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

        return det
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
         # TODO - your code here
        else:
            return sum([self.g[i][i] for i in range(self.h)])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        elif self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        # TODO - your code here
        else:   
            inverse = [[1 / self.determinant() for _ in range(self.w)] for __ in range(self.h)]
            if self.h == 2:
                inverse[0][0] *=  self.g[1][1]
                inverse[0][1] *= -self.g[0][1]
                inverse[1][0] *= -self.g[1][0]
                inverse[1][1] *=  self.g[0][0]        
            return Matrix(inverse)
        
    def T(self):  
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here    
        return Matrix([[self[i][j] for i in range(self.h)] for j in range(self.w)])
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:        
            return Matrix([[self.g[j][i] + other.g[j][i] for j in range(0, self.h)] for i in range(0, self.w)])
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        return Matrix([[self.g[j][i] * -1 for j in range(self.h)] for i in range(self.w)])
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        else:
            return Matrix([[self.g[j][i] - other.g[j][i] for j in range(self.h)] for i in range(self.w)])
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if the both matrix are same height") 
        else:
            mul = [[1.0 for _ in range(other.w)] for __ in range(self.h)]
            for i in range(self.h):
                for j in range(other.w):
                    dot_product = 0
                    for k in range(other.h):
                        dot_product += self[i][k] * other[k][j]
                    mul[i][j] = dot_product            
                    
            return Matrix(mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            return Matrix([[self.g[j][i] * other for j in range(self.h)] for i in range(self.w)])

           
            
            
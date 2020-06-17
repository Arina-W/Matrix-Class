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
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        if len(grid) == 1  and len(grid[0]) == 1:
            det = grid[0][0]
            return det
                   
        elif (grid[0][0] * grid[1][1] - grid[0][1] * grid[1][0]) == 0:
            raise ValueError('The denominator of a fraction cannot be zero')
        
        elif len(grid) == 2  and len(grid[0]) == 2:
            det = (grid[0][0] * grid[1][1] - grid[0][1] * grid[1][0])
            return det        
        
        else: 
            print ('Fix your det code')

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        sum = 0
        
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    sum += self[i][j]
                else:
                    None
        return sum
 

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        inverse = []
        
        if self.h == 1  and self.w == 1:
            row = []
            for i in range(self.h):
                a = 1/self[0][0]
                row.append(a)
            inverse.append(row)
        
        elif (self[0][0] * self[1][1] - self[0][1] * self[1][0]) == 0:
            raise ValueError('The denominator of a fraction cannot be zero')
        
        elif self.h == 2  and self.w == 2:
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    a = 1/ (self[0][0] * self[1][1] - self[0][1] * self[1][0])
                    x = a * self[i][j]               
                    row.append(x)
                inverse.append(row)
        
            inverse[0][0] , inverse[1][1] = inverse[1][1] , inverse[0][0] 
            inverse[0][1] = -inverse[0][1]
            inverse[1][0] = -inverse[1][0]       
        
        else: 
            print ('Fix your code')
    
        return Matrix(inverse)
    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

        matrix_transpose = []
        
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self[j][i])
            matrix_transpose.append(row)
    
        return Matrix(matrix_transpose)        
    

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

        matrixSum = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                r = self[i][j] + other[i][j]
                row.append(r)
            matrixSum.append(row)
        return Matrix(matrixSum)
        

    def __neg__(self):
        
        negat = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                a = self[i][j] * -1
                row.append(a)
            negat.append(row)               
        return Matrix(negat)

        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
   
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                r = self[i][j] - other[i][j]
                row.append(r)
            matrixSub.append(row)
        return Matrix(matrixSub)
               
        
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        def get_row(self, row):
            return self[row]
        
        def get_column(self, column_number):
            column = []
            for i in range(self.h):
                column.append(self[i][column_number])            
            return column

        def dot_product(vector_one, vector_two):
            vecprods = []
            for i in range(len(vector_one)):
                prods = vector_one[i] * vector_two[i]
                vecprods.append(prods)

            return sum(vecprods)
        
    
        # empty list that will hold the product of AxB
        result = []
        for i in range(self.h):
            row_result = []
            for j in range(other.w):
                a = get_row(self, i) 
                b = get_column(other, j)
                c = dot_product(a, b)  
                row_result.append(c)
            result.append(row_result)
        return Matrix(result)
        
        
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
            rmul = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    x = other * self[i][j]               
                    row.append(x)
                rmul.append(row)
            return Matrix(rmul)
        else:
            None

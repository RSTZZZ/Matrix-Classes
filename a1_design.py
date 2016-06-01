class Matrix():
    '''A class to represent the data structure Matrix. This
    Matrix can be used like the ones we see in Math classes
    but can also hold objects other than numbers'''

    def __init__(self, data, row=None, column=None):
        '''(Matrix, list of list of obj, Int, Int) -> NoneType
        This is an automatically run method. This starts up
        the class Matrix. The class Matrix takes in data, in the
        format of lists. Regardless of the data inside, it will
        take up only the first row * column data. A row will be one
        line of the file, and it will take up column amount of objects
        per line. if last two not specified, it will take up all
        data given.
        REQ: row > 0 , column > 0
        REQ: list must have row lists and column elements
        '''
        pass

    def multiply(self, obj):
        '''(Matrix, Int/Matrix) -> Matrix
        This is a method that allows a scalar multiplication or
        the multiplication between two matrices. It can decide whether
        it is a scalar or between matrices, so don't worry. XD
        REQ: if matrix, both matrices' element must be numeric
        REQ: if matrix, and if matrix1 is m by n, then matrix2 must be
            n * k
        '''
        pass

    def subtract(self, obj):
        '''(Matrix, Matrix) -> Matrix
        This is a method that allows the user to subtract matrices.
        REQ: both matrices's element must be numeric
        REQ: if matrix1 is m by n, then matrix 2 must also be m by n
        '''
        pass

    def add(self, obj):
        '''(Matrix, Matrix) -> Matrix
        This is a method that allows users to add two matrices. This
        addition is very special. It can add two objects, regardless,
        as long as their is a str representation of this obj. The element
        that is returned will either be numeric (if adding two numbers) or
        str (adding two objects other than int/float)
        REQ: if matrix1 is m by n, then matrix2 must also be m by n
        '''
        pass

    def get_column(self, column_num=1):
        '''(Matrix, Int) -> List of Obj
        This is a method that allows users to get the wanted column.
        REQ: column_num > 0
        REQ: column_num <= num of columns in Matrix
        '''
        pass

    def set_column(self, data, column_num=1):
        '''(Matrix, List of Obj, Int) -> Matrix
        This is a method that allows users to override a column.
        REQ: column_num > 0
        REQ: column_num <= num of columns in Matrix
        REQ: List of Obj = num of rows in Matrix
        '''
        pass

    def get_row(self, row_num=1):
        '''(Matrix, Int) -> List of Obj
        This is a method that allows users to get the wanted row.
        REQ: row_num > 0
        REQ: row_num <= num of row in Matrix
        '''
        pass

    def set_row(self, data, row_num=1):
        '''(Matrix, List of Obj, Int) -> Matrix
        This is a method that allows users to override a row.
        REQ: row_num > 0
        REQ: row_num <= num of row in Matrix
        REQ: List of Obj = num of columns in Matrix
        '''
        pass

    def get(self, row=1, column=1):
        '''(Matrix, Int, Int) -> Obj
        This is a method that allows users to retrieve an element.
        REQ: row > 0 and row <= # of rows in Matrix
        REQ: column > 0 and column <= # of rows in Matrix
        '''
        pass

    def set(self, obj, row=1, column=1):
        '''(Matrix, Obj, Int, Int) -> Matrix
        This is a method that allows users to set an element.
        REQ: row > 0 and row <= # of rows in Matrix
        REQ: column > 0 and column <= # of rows in Matrix.
        '''
        pass

    def swap_rows(self, row1, row2):
        '''(Matrix, Int, Int) -> Matrix
        This is a method that allows users to swap two rows.
        REQ: row1 > 0 and row1 <= # of rows in Matrix
        REQ: row2 > 0 and row2 <= # of rows in Matrix
        (Yes, this is possible row1 == row2)
        '''
        pass

    def swap_columns(self, column1, column2):
        '''(Matrix, Int, Int) -> Matrix
        This is a method that allow users to swap two columns.
        REQ: column1 > 0 and column1 <= # of columns in Matrix
        REQ: column2 > 0 and column2 <= # of columns in Matrix
        '''
        pass

    def determinant(self):
        '''(Matrix) -> Float/ Int
        This is a method that finds the determinant of a matrix.
        REQ: This matrix must be 2 by 2 (for some odd reason)
        '''
        pass

    def transpose(self):
        '''(Matrix) -> Matrix
        This is a method that transposes a matrix. This means an element
        at row i, column j, become the element at row j, column i.
        '''
        pass

    def __str__(self):
        '''(Matrix) -> str
        This is a method that gives a string representation of the Matrix.
        It will be written row by row.
        '''
        pass

    def _is_numeric(self):
        '''(Matrix) -> bool
        This is a private method. Note: PRIVATE. This method is used
        to allow the class matrix to determine if the whole Matrix is numeric
        or not. This is to help the methods multiply and subtract.
        '''
        pass


class SquareMatrix(Matrix):
    '''A class to represent a square matrix'''

    def __init__(self, data, row=1):
        '''(SquareMatrix, list of list of obj, Int) -> None
        This is an automated method.
        REQ: row > 0
        REQ: list must have row lists with row elements
        '''
        pass

    def get_diagonal(self):
        '''(SquareMatrix) -> List of Obj
        This is a method that returns the diagonal elements in the
        SquareMatrix.
        '''
        pass

    def multiply(self, obj):
        '''(SquareMatrix, Int/Matrix) -> SquareMatrix
        This is a method that allows a scalar multiplication or
        the multiplication between two matrices. It can decide whether
        it is a scalar or between matrices, so don't worry. XD
        It will preserve the original row by row size.
        REQ: if matrix, both matrices' element must be numeric
        REQ: if matrix, and if matrix1 is n by n, then matrix2 must be
            n * k
        '''
        pass

    def swap(self, rc1, number1, rc2, number2):
        '''(SquareMatrix, str, int, str, int) -> SquareMatrix
        This is a method that allows the swapping of a row with a row
        row with column, column with column and column with row.
        REQ: rc = r or c, rc2 = r or c
        REQ: number1 > 0, number2 > 0
        REQ: number1 < amount of rows, number2 < amount of rows
        '''


class SymmetricMatrix(SquareMatrix):
    '''A class to represent a symmetric matrix'''

    def __init__(self, data, row=1):
        '''(SymmetricMatrix, list of list of obj, int) -> None
        This is an automated method.
        (make sure it is symmetric)
        The resulting matrix is n by n.
        REQ: list must have row lists and row elements.
        '''
        pass

    def multiply(self, obj):
        '''(SymmetricMatrix, Int/Matrix) -> SymmetricMatrix
        This is a method that allows a scalar multiplication or
        the multiplication between two matrices. It can decide whether
        it is a scalar or between matrices, so don't worry. XD
        It will take the first lower half and make it symmetric.
        REQ: if matrix, both matrices' element must be numeric
        REQ: if matrix, and if matrix1 is n by n, then matrix2 must be
            n * k
        '''
        pass

    def subtract(self, obj):
        '''(SymmetricMatrix, Matrix) -> SymmetricMatrix
        This is a method that allows the user to subtract matrices.
        It will take the first lower half and make it symmetric.
        REQ: both matrices's element must be numeric
        REQ: if matrix1 is n by n, then matrix 2 must also be n by n
        '''
        pass

    def add(self, obj):
        '''(SymmetricMatrix, Matrix) -> SymmetricMatrix
        This is a method that allows users to add two matrices. This
        addition is very special. It can add two objects, regardless,
        as long as their is a str representation of this obj. The element
        that is returned will either be numeric (if adding two numbers) or
        str (adding two objects other than int/float)
        It will take the first lower half and make it symmetric.
        REQ: if matrix1 is n by n, then matrix2 must also be n by n
        '''
        pass

    def set(self, obj, row=1, column=1):
        '''(SymmetricMatrix, obj, Int, Int) -> SymmetricMatrix
        This method will override whatever it is on element at row and
        column. It will also override whatever is on element column and
        row.
        REQ: row > 0 and row <= num of rows in matrix
        REQ: column > 0 and column <= num of coloumn in matrix
        '''
        pass

    def set_row(self, data, row=1):
        '''(SymmetricMatrix, List of Obj, Int) -> SymmetricMatrix
        This method will override whatever it is in that row.
        It will change the corresponding elements to make it symmetric.
        REQ: row > 0 and row <= num of rows in matrix
        REQ: len(List of obj) == num of rows in matrix
        '''
        pass

    def set_column(self, data, column=1):
        '''(SymmetricMatrix, List of Obj, Int) -> SymmetricMatrix
        This method will override whatever it is in that column.
        It will change the corresponding elements to make it symmetric.
        REQ: column > 0 and column <= num of coloumn in matrix
        REQ: len(List of obj) == num of rows in matrix
        '''
        pass

    def swap_rows(self, row1, row2):
        '''(SymmetricMatrix, Int, Int) -> SymmetricMatrix
        This method will swap two rows.
        It will then use the first lower half and make the rest symmetric
        to it.
        REQ: row1 > 0 and row1 <= num of rows in matrix
        REQ: row2 > 0 and row2 <= num of rows in matrix
        '''
        pass

    def swap_columns(self, column1, column2):
        '''(SymmetricMatrix, Int, Int) -> SymmetricMatrix
        This method will swap two columns.
        It will then use the first lower half and make the rest symmetric
        to it.
        REQ: column1 > 0 and column1 <= num of columns in matrix
        REQ: column2 > 0 and column2 <= num of columns in matrix
        '''
        pass

    def _make_symmetric(self):
        '''(SymmetricMatrix) -> SymmetricMatrix
        This method will use the first lower half triangles and make
        the matrix into a symmetric matrix. This is a helper method.
        '''
        pass


class DiagonalMatrix(SymmetricMatrix):
    '''A class to represent an diagonal Matrix'''

    def __init__(self, obj, row=1):
        '''(DiagonalMatrix, obj, int) -> None
        This matrix can take in an obj. It will repeat the obj on
        all diagonal for the row by row matrix.
        REQ: row > 0
        '''
        pass

    def multiply(self, obj):
        '''(DiagonalMatrix, Int/Matrix) -> DiagonalMatrix
        This is a method that allows a scalar multiplication or
        the multiplication between two matrices. It can decide whether
        it is a scalar or between matrices, so don't worry. XD
         It will take the diagonal and make it a diagonal matrix.
        REQ: if matrix, both matrices' element must be numeric
        REQ: if matrix, and if matrix1 is n by n, then matrix2 must be
            n * k
        '''
        pass

    def subtract(self, obj):
        '''(DiagonalMatrix, Matrix) -> DiagonalMatrix
        This is a method that allows the user to subtract matrices.
        It will take the diagonal and make it a diagonal matrix.
        REQ: both matrices's element must be numeric
        REQ: if matrix1 is n by n, then matrix 2 must also be n by n
        '''
        pass

    def add(self, obj):
        '''(DiagonalMatrix, Matrix) -> DiagonalMatrix
        This is a method that allows users to add two matrices. This
        addition is very special. It can add two objects, regardless,
        as long as their is a str representation of this obj. The element
        that is returned will either be numeric (if adding two numbers) or
        str (adding two objects other than int/float)
         It will take the diagonal and make it a diagonal matrix.
        REQ: if matrix1 is n by n, then matrix2 must also be n by n
        '''
        pass

    def set(self, obj, row=1, column=1):
        '''(DiagonalMatrix, obj, Int, Int) -> None
        This method will override whatever it is on element at row and
        column. It will also override whatever is on element column and
        row.
        It will take the diagonal and make it a diagonal matrix.
        REQ: row > 0 and row <= num of rows in matrix
        REQ: column > 0 and column <= num of coloumn in matrix
        '''
        pass

    def set_row(self, data, row=1):
        '''(DiagonalMatrix, List of Obj, Int) -> None
        This method will override whatever it is in that row.
         It will take the diagonal and make it a diagonal matrix.
        REQ: row > 0 and row <= num of rows in matrix
        REQ: len(List of obj) == num of rows in matrix
        '''
        pass

    def set_column(self, data, column=1):
        '''(DiagonalMatrix, List of Obj, Int) -> None
        This method will override whatever it is in that column.
         It will take the diagonal and make it a diagonal matrix.
        REQ: column > 0 and column <= num of coloumn in matrix
        REQ: len(List of obj) == num of rows in matrix
        '''
        pass

    def swap_rows(self, row1, row2):
        '''(DiagonalMatrix, Int, Int) -> None.
        This method will swap two rows.
        It will take the diagonal and make it a diagonal matrix.
        REQ: row1 > 0 and row1 <= num of rows in matrix
        REQ: row2 > 0 and row2 <= num of rows in matrix
        '''
        pass

    def swap_columns(self, column1, column2):
        '''(DiagonalMatrix, Int, Int) -> None.
        This method will swap two columns.
        It will take the diagonal and make it a diagonal matrix.
        REQ: column1 > 0 and column1 <= num of columns in matrix
        REQ: column2 > 0 and column2 <= num of columns in matrix
        '''
        pass

    def _make_identical(self):
        '''(DiagonalMatrix) -> IdentityMatrix
        It will take the diagonal and make it an diagonal matrix.
        This is a helper method.
        '''
        pass


class IdentityMatrix(DiagonalMatrix):
    '''A class to represent a identical Matrix'''

    def __init__(self, row=1):
        '''(identicalMatrix, int) -> None
        This matrix can take in an obj. It will repeat 1's on
        all diagonal for the row by row matrix.
        REQ: row > 0
        '''
        pass


class MatrixNotNumber(Exception):
    '''An exception that represents all the illegal moves
    that is raised when the matrix is not all numbers'''


class MatrixNot2By2(Exception):
    '''An exception that represents when finding determinant
    but it is not 2 by 2'''


class MatrixOutOfBound(Exception):
    '''An exception that represents all the getters and setters
    when it cannot find that element, row, or column'''


class MatrixIllegalMove(Exception):
    '''An exception that represents the limitations of Matrix.
    This rasies only become row by column errors, making such
    move not possible.'''

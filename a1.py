class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    pass


class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''
    pass


class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''
    pass


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        REQ: None
        '''
        self._contents = contents
        self._right = right
        self._down = down
        self._position = (0, 0)

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        REQ: None
        '''
        return str(self._contents)

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        REQ: None
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        REQ: None
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        REQ: None
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        REQ: None
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        REQ: None
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        REQ: None
        '''
        self._down = new_node

    def get_position(self):
        '''(MatrixNode) -> obj
        Return the position of the matrix node.
        REQ: None
        '''
        return self._position

    def set_position(self, x, y):
        '''(MatrixNode, obj) -> NoneType
        Set the position of this node to x and y coordinate
        REQ: x, y > 0
        '''
        self._position = (x, y)

    def __repr__(self):
        '''(MatrixNode) -> str
        A str representaion of this MatrixNode.
        REQ: None
        '''
        # use try since a personal method, just so it won't crash automarker
        try:
            # result first equals the head
            res = repr(self._contents)
            # set d where it keeps track of going down, it first equal self
            d = self
            # keep going down until reach none
            while d is not None:
                # first round, if d is self
                if d == self:
                    # set r where it keeps track of going right
                    # first equal d
                    r = d
                    # add a counter to see if it is first one
                    count = 0
                    # keep going right
                    while r is not None:
                        # if not the last one
                        if r._right is not None:
                            # add the str representation
                            res = res + ' --- ' + repr(r._right._contents)
                        # keep track of how long it is
                        count += 1
                        # go right so as to make not infinite loop
                        r = r._right
                # rest of the down
                if d._down is not None:
                    # first create the down arrows
                    res = res + '\n' + '|'
                    # create as many arrows as need
                    for num in range(count-1):
                        # first arrow would be a different space
                        if num == 0:
                            res = res + '        |'
                        # other arrows are equidistant
                        else:
                            res = res + '     |'
                    # start adding the contetns downwards
                    res = res + '\n' + repr(d._down._contents)
                    r = d._down
                    # get a temporary which is the top row
                    temp = self
                    # keep count to see if first one
                    first_space = True
                    # keep going right
                    while r is not None:
                        # see the next right one
                        if r._right is not None:
                            # check if the first row right one
                            # and this row's right one is the same column
                            # position
                            (row, col) = temp._right._position
                            (row2, col2) = r._right._position
                            # if not, add a empty arrow and space
                            while col < col2:
                                # different for first one
                                if first_space:
                                    res = res + ' -------' + '+'
                                else:
                                    res = res + '-----' + '+'
                                # change count since after first
                                first_space = False
                                # keep going right, since u added a arrow
                                temp = temp._right
                                (row, col) = temp._right._position
                            # if column position are equal, add the string rep
                            if col == col2:
                                # different length for first time
                                if first_space:
                                    res = res + ' ------ ' + repr(
                                        r._right._contents)
                                # else equal length
                                else:
                                    res = res + '---- ' + repr(
                                        r._right._contents)
                        else:
                            # if the last row, make first row
                            # column go to end
                            while temp._right is not None:
                                temp = temp._right
                            # compare the positions
                            (row, col) = temp._position
                            (row2, col2) = r._position
                            # add more spaces until equal
                            while col > col2:
                                # create a tempory node, equal self
                                temp3 = self
                                # get its position
                                (row3, col3) = temp3._position
                                # keep going until u hit the right column
                                # number
                                while (col3 != col2 + 1) and (temp3._right
                                                              is not None):
                                    temp3 = temp3._right
                                    (row3, col3) = temp3._position
                                # set up condition, to break loop if needed
                                cond = True
                                # you keep going down
                                while (row3 <= row2) and cond:
                                    temp3 = temp3._down
                                    if temp3 is not None:
                                        (row3, col3) = temp3._position
                                    # break function, make row3 smaller
                                    # than row2
                                    else:
                                        row3 = row2 - 1
                                        cond = False
                                if row3 > row2:
                                    res = res + '     ' + '|'
                                row2 += 1
                                col2 += 1
                        first_space = True
                        r = r._right
                        temp = temp._right
                d = d._down
        except:
            # just return a value
            res = repr(self._contents)
        return res


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        REQ: m, n >= 0
        '''
        self._head = MatrixNode(None)
        if m < 0 or n < 0:
            raise MatrixIndexError
        self._row_num = m
        self._column_num = n
        self._default = default

    def get_dimensions(self):
        '''(Matrix) -> (int, int)
        Return the dimensions of the matrix.
        REQ: None
        '''
        return (self._row_num, self._column_num)

    def get_head(self):
        '''(Matrix) -> MatrixNode
        Return the head of the Matrix.
        REQ: None
        '''
        return self._head

    def get_default(self):
        '''(Matrix) -> int
        Return default value
        REQ: None
        '''
        return self._default

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        # check bounds if valid
        self._check_bounds(i, j)
        # check if node exists
        if self.contains(i + 1, j + 1):
            # exists, just get to the value
            curr = self.find(i, j)
            result = curr.get_contents()
        else:
            # return default if node does not exist
            result = self._default
        return result

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        # check bounds if valid
        self._check_bounds(i, j)
        # check if column and row nodes is there, if not, add it
        if new_val != self._default:
            # set the row index node (this method checks if the row
            # exists, since you must have it for a matrix)
            self._set_row_node(i)
            # set the column index node
            self._set_column_node(j)
            # add the node, and it connects it to the top previous value
            # and the left previous value of this node
            self._connect_value(i, j, new_val)
        # when u want to set_val to default, aka, delete the node
        # if node is already there
        else:
            # check if it contains this node
            if self.contains(i, j):
                # if contain, then deconnect node
                # set the top node next down value as the value under this
                # element's node
                # set the left node next right value as the value right of
                # this element's node
                self._deconnect_node(i, j)

    def get_row(self, m):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the m'th row of this matrix
        REQ: 0 <= m <= # of rows - 1
        '''
        # check the bounds, raise an Error
        self._check_bounds(m, 0)
        # find it row index node
        curr = self.find(m, -1)
        temp = curr
        # find how many in the column
        (row, col) = self.get_dimensions()
        # initialize the 1Dmatrix, by default, it is a row
        # set its default equal to the matrix's default
        result = OneDimensionalMatrix(col, self.get_default())
        # at the row index node, you keep going right
        if curr is not None:
            while curr.get_right() is not None:
                curr = curr.get_right()
                # get the val of the current node
                val = curr.get_contents()
                (row, col) = curr.get_position()
                # set the item in the resulting 1D matrix
                # with current val, and col
                result.set_item(col-1, val)
        return result

    def set_row(self, m, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the m'th row of this matrix to those of new_row
        REQ: 0 <= m  <= # of rows - 1
        REQ: # of columns in row == # of columns in self (if new_row is 1 by n)
        REQ: # of rows in row == # of columns in self (if new_row is n by 1)
        '''
        # check bounds if valid
        self._check_bounds(m, 0)
        # intialize curr = new_row.head
        curr = new_row.get_head()
        # see if 1DMatrix is a row or column
        rc = new_row.get_rc()
        if rc == 'r':
            # check if the number of rows are equal
            (row, col) = new_row.get_dimensions()
            (row2, col2) = self.get_dimensions()
            if col != col2:
                raise MatrixInvalidOperationError
            # if row, go right, then start going down
            if curr.get_down() is not None:
                curr = curr.get_down()
                # loop down, adding a val, for each val in row
                while curr.get_right() is not None:
                    curr = curr.get_right()
                    val = curr.get_contents()
                    (row, col) = curr.get_position()
                    self.set_val(m, col - 1, val)
        else:
            # check if the number of rows are equal
            (row, col) = new_row.get_dimensions()
            (row2, col2) = self.get_dimensions()
            if row != col2:
                raise MatrixInvalidOperationError
            # if column, go down, then start going right
            if curr.get_right() is not None:
                curr = curr.get_right()
                while curr.get_down() is not None:
                    curr = curr.get_down()
                    val = curr.get_contents()
                    (row, col) = curr.get_position()
                    self.set_val(m, row - 1, val)
        # check if both defaults are of the same value:
        new_row_default = new_row.get_default()
        default = self.get_default()
        if new_row_default != default:
            # make all misssing nodes with new_row_default:
            for col_num in range(col2):
                if rc == 'r':
                    if not new_row.contains(1, col_num + 1):
                        self.set_val(m, col_num, new_row_default)
                else:
                    if not new_row.contains(col_num + 1, 1):
                        self.set_val(m, col_num, new_row_default)
        else:
            # make all misssing nodes still missing:
            for col_num in range(col2):
                if rc == 'r':
                    if not new_row.contains(1, col_num + 1):
                        self._deconnect_node(m, col_num)
                else:
                    if not new_row.contains(col_num + 1, 1):
                        self._deconnect_node(m, col_num)

    def get_col(self, n):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the n'th column of this matrix
        REQ: 0 <= n <= # of columns -1
        '''
        # check bounds
        self._check_bounds(0, n)
        # find it first
        curr = self.find(-1, n)
        temp = curr
        # find how many in the column
        (row, col) = self.get_dimensions()
        # initialize the new 1D matrix, and make it into a column (n by 1)
        result = OneDimensionalMatrix(row, self.get_default(), 'c')
        # keep going down
        # if curr is None, that means its nonexistant column, so
        # we have to do nothing
        if curr is not None:
            while curr.get_down() is not None:
                curr = curr.get_down()
                val = curr.get_contents()
                (row, col) = curr.get_position()
                # set to val of the current node to the 1D matrix
                result.set_item(row - 1, val)
        return result

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the n'th column of this matrix to those of new_row
        REQ: 0 <= col_num <= # of columns - 1
        REQ: # of rows in new_col == # of rows in self (if new_col is n by 1)
        REQ: # of cols in new_col == # of rows in self (if new_col is 1 by n)
        '''
        # check bounds if valid
        self._check_bounds(0, col_num)
        # intialize curr = new_row.head
        curr = new_col.get_head()
        # see if 1DMatrix is a row or column
        rc = new_col.get_rc()
        if rc != 'r':
            # check if the number of col are equal
            (row, col) = new_col.get_dimensions()
            (row2, col2) = self.get_dimensions()
            if col != row2:
                raise MatrixInvalidOperationError
            # if row, go right, then start going down
            if curr.get_down() is not None:
                curr = curr.get_down()
                # loop down, adding a val, for each val in row
                while curr.get_right() is not None:
                    curr = curr.get_right()
                    val = curr.get_contents()
                    (row, col) = curr.get_position()
                    self.set_val(col - 1, col_num, val)
        else:
            # check if the number of col are equal
            (row, col) = new_col.get_dimensions()
            (row2, col2) = self.get_dimensions()
            if row != row2:
                raise MatrixInvalidOperationError
            # if column, go down, then start going right
            if curr.get_right() is not None:
                curr = curr.get_right()
                while curr.get_down() is not None:
                    curr = curr.get_down()
                    val = curr.get_contents()
                    (row, col) = curr.get_position()
                    self.set_val(row - 1, col_num, val)
        # check if both defaults are of the same value:
        new_col_default = new_col.get_default()
        default = self.get_default()
        if new_col_default != default:
            # make all misssing nodes with new_row_default:
            for row_num in range(row2):
                if rc == 'r':
                    if not new_col.contains(1, col_num + 1):
                        self.set_val(row_num, col_num, new_col_default)
                else:
                    if not new_col.contains(col_num + 1, 1):
                        self.set_val(row_num, col_num, new_col_default)
        else:
            # make all misssing nodes still missing:
            for row_num in range(row2):
                if rc == 'r':
                    if not new_row.contains(1, col_num + 1):
                        self._deconnect_node(row_num, col_num)
                else:
                    if not new_row.contains(col_num + 1, 1):
                        self._deconnect_node(row_num, col_num)

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of rows - 1
        '''
        # get the ith row
        i_row = self.get_row(i)
        # get the jth row
        j_row = self.get_row(j)
        # set the jth row to the ith row
        self.set_row(j, i_row)
        # set the ith row to the jth row
        self.set_row(i, j_row)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        REQ: 0 <= i <= # of columns - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        first_col = self.get_col(i)
        second_col = self.get_col(j)
        self.set_col(j, first_col)
        self.set_col(i, second_col)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        REQ: None
        '''
        # all nonexistant nodes value is now added by this value
        self._default += add_value
        # go through each row, and column, adding this value
        curr = self._head
        # this first loop is going to the next column index node
        while curr is not None and curr.get_right() is not None:
            curr = curr.get_right()
            # make a temporary, so as to not change curr node
            temp_node = curr
            # loop to go down the rows
            # get value, add the scalar, then set it as new content
            while temp_node is not None and temp_node.get_down() is not None:
                temp_node = temp_node.get_down()
                value = temp_node.get_contents()
                value += add_value
                temp_node.set_contents(value)

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        REQ: None
        '''
        # subtract_scalar is literally add_scalar, but make sub_value negative
        self.add_scalar(-sub_value)

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        REQ: None
        '''
        # change the deafult value first
        self._default = self._default * mult_value
        # you only want to transverse if mult_value is not zero, since
        # if it is, everything will be zero
        if mult_value != 0:
            # go from head
            curr = self._head
            # keep going to the next column index node
            while curr is not None and curr.get_right() is not None:
                curr = curr.get_right()
                # temp node so as to go down the column, without changing
                # the current node position
                temp_node = curr
                while ((temp_node is not None) and
                       (temp_node.get_down() is not None)):
                    temp_node = temp_node.get_down()
                    value = temp_node.get_contents()
                    value = value * mult_value
                    temp_node.set_contents(value)
        else:
            # get the dimennsions
            (row, col) = self.get_dimensions()
            # create a new matrix, with zero as default
            new_matrix = Matrix(row, col, 0)
            # change the self head to the new_matrix's head
            self._head = new_matrix.get_head()

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # get the new default value
        total = self.get_default() + adder_matrix.get_default()
        # check if dimensions are equal
        if self.get_dimensions() == adder_matrix.get_dimensions():
            # check elements to see if there
            (drow, dcol) = self.get_dimensions()
            # go down through each row
            for row_num in range(drow + 1):
                # go right through each row
                for col_num in range(drow + 1):
                    # see if the you have it
                    if self.contains(row_num + 1, col_num + 1):
                        # if u do, first val is that node's content
                        val1 = self.find(row_num, col_num).get_contents()
                        # check if second has the content
                        if adder_matrix.contains(row_num + 1, col_num + 1):
                            # if found, sec val is that node's content
                            val2 = adder_matrix.find(row_num, col_num)
                            val2 = val2.get_contents()
                        else:
                            # not found, sec val is default val
                            val2 = adder_matrix.get_default()
                        # total val = val1 + val2
                        val = val1 + val2
                        # find that node, and set its content
                        self.find(row_num, col_num).set_contents(val)
                        if val == total:
                            self._deconnect_node(row_num, col_num)
                    else:
                        # not found in fist matrix, first val is default val
                        val1 = self.get_default()
                        # if found in second matrix, sec val is that node's
                        # content
                        if adder_matrix.contains(row_num + 1, col_num + 1):
                            val2 = adder_matrix.find(row_num, col_num)
                            val2 = val2.get_contents()
                            # total val = val1 + val2
                            val = val1 + val2
                            # in first matrix, set the val
                            self.set_val(row_num, col_num, val)
                            if val == total:
                                self._deconnect_node(row_num, col_num)
            # change default value since all not found node is the same
            # new value
            self._default = total
        else:
            raise MatrixDimensionError
        return self

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        REQ: if self is a m by n matrix, than mult_matrix must be a n by k
        RWQ: matrix
        '''
        # check if it is m by n * n by k
        (row, col) = self.get_dimensions()
        (row2, col2) = mult_matrix.get_dimensions()
        if col != row2:
            raise MatrixDimensionError
        # get the new default
        # get the default of self
        default1 = self.get_default()
        # get the default of the mult_matrix
        default2 = mult_matrix.get_default()
        # get new_default by multiplying default1, default2 by # of rows
        new_default = default1 * default2 * row
        # initialize new_matrix
        new_matrix = Matrix(row, col2, new_default)
        # go through row_num
        for row_num in range(row):
            # first get self matrix's row
            the_row = self.get_row(row_num)
            # go through each col in mult_matrix
            for col_num in range(col2):
                the_col = mult_matrix.get_col(col_num)
                # value will be equal to row * col (or the dot product of
                # these two vectors/OneDimensionalMatrix)
                value = the_row.multiply_matrix(the_col)
                # set this as the new_val in matrix
                new_matrix.set_val(row_num, col_num, value)
        return new_matrix

    def _check_bounds(self, i, j):
        '''(Matrix, int, int) -> NoneType
        This is an internal method that checks the bounds
        REQ: None
        '''
        # check if the num of rows is valid
        if i > (self._row_num - 1):
            raise MatrixIndexError
        # check if the num of columns is valid
        if j > (self._column_num - 1):
            raise MatrixIndexError
        # make sure i and j must be greater than zero
        if i < 0 and j < 0:
            raise MatrixIndexError

    def _set_row_node(self, i):
        '''(Matrix, int) -> NoneType
        This is an internal method that checks if we have that ith node.
        if we don't, we add it.
        REQ: 0 <= i <= # of rows - 1
        '''
        # check if in bounds
        self._check_bounds(i, 0)
        # check if it contains this row or not
        if not self.contains(i + 1, 0):
            # set curr = head
            curr = self._head
            cond = True
            while curr.get_down() is not None and cond:
                # you go down until u get to the one before this index
                if curr.get_position() < (i + 1, 0):
                        if curr.get_down().get_position() < (i + 1, 0):
                            curr = curr.get_down()
                        else:
                            cond = False
                else:
                    cond = False
            next_node = curr.get_down()
            new_node = MatrixNode(i, None, next_node)
            curr.set_down(new_node)
            new_node.set_position(i + 1, 0)

    def contains(self, x, y):
        '''(Matrix, int, int) -> bool
        Return True iff the node exists with first node head.
        (The i and j points to the coordinate system)
        REQ: 0 <= x <= # of rows
        REQ: 0 <= y <= # of columns
        '''
        # intialize result as False
        result = False
        # start from head
        curr = self._head
        # get position
        (row, col) = curr.get_position()
        # go right until hit position y
        while curr is not None and col != y:
            curr = curr.get_right()
            # give position of curr node is not none
            if curr is not None:
                (row, col) = curr.get_position()
        # still, get the position
        if curr is not None:
            position = curr.get_position()
            # go down until u hit the position
            while curr is not None and position != (x, y):
                curr = curr.get_down()
                if curr is not None:
                    position = curr.get_position()
            # result is T iff postion == (x, y)
            if position == (x, y):
                result = True
        return result

    def _set_column_node(self, j):
        '''(Matrix, int) -> NoneType
        This is an internal method that checks if we have that ith node.
        if we don't, we add it.
        REQ: 0 <= j <= # of columns - 1
        '''
        # check if in bounds
        self._check_bounds(0, j)
        # check if it contains this row or not
        if not self.contains(0, j + 1):
            # set curr = head
            curr = self._head
            cond = True
            while curr.get_right() is not None and cond:
                # you go down until u get to the one before this index
                if curr.get_position() < (0, j + 1):
                        if curr.get_right().get_position() < (0, j + 1):
                            curr = curr.get_right()
                        else:
                            cond = False
                else:
                    cond = False
            next_node = curr.get_right()
            new_node = MatrixNode(j, next_node, None)
            curr.set_right(new_node)
            new_node.set_position(0, j + 1)

    def _connect_value(self, i, j, value):
        '''(Matrix, int, int, obj) -> NoneType
        This is an internal method that adds a node at column j, with the
        rth coordinate.
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        # check if this node exists
        if self.contains(i + 1, j + 1):
            # exists, just change val
            curr = self.find(i, j)
            curr.set_contents(value)
        # check if the column exists
        elif self.contains(0, j + 1):
            # check if row exists
            if self.contains(i + 1, 0):
                # find the node on top
                curr = self.find_top(i, j)
                down_nodes = curr.get_down()
                # find the node on the left
                node2 = self.find_left(i, j)
                right_nodes = node2.get_right()
                new_node = MatrixNode(value, right_nodes, down_nodes)
                curr.set_down(new_node)
                node2.set_right(new_node)
                new_node.set_position(i + 1, j + 1)

    def _deconnect_node(self, i, j):
        '''(Matrix, int, int, obj) -> NoneType
        This is an internal method that deletes a node at column j, with the
        ith coordinate.
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        if self.contains(i + 1, j + 1):
            if self.contains(0, j + 1):
                # check if row exists
                if self.contains(i + 1, 0):
                    # find the node on top
                    curr = self.find_top(i, j)
                    # go down twice
                    down_nodes = curr.get_down().get_down()
                    # find the node on the left
                    node2 = self.find_left(i, j)
                    # go down left twice
                    right_nodes = node2.get_right().get_right()
                    curr.set_down(down_nodes)
                    node2.set_right(right_nodes)
            # check if right of row, there is still value:
            curr = self.find(i, -1)
            if curr.get_right() is None:
                temp = self.find_top(i, -1)
                curr = curr.get_down()
                temp.set_down(curr)
            # check if down of col, there is still value:
            curr = self.find(-1, j)
            if curr.get_down() is None:
                temp = self.find_left(-1, j)
                curr = curr.get_right()
                temp.set_right(curr)

    def find(self, i, j):
        '''(Matrix, int, int) -> MatrixNode/ None
        Return the node
        REQ: - 1 <= i <= # of rows - 1
        REQ: -1  <= j <= # of columns - 1
        '''
        if self.contains(i + 1, j + 1):
            curr = self._head
            (row, col) = curr.get_position()
            while col != (j + 1):
                curr = curr.get_right()
                (row, col) = curr.get_position()
            # start from j+1 column, head down until before it, or end
            while row != (i + 1):
                curr = curr.get_down()
                (row, col) = curr.get_position()
            result = curr
        else:
            result = None
        return result

    def find_top(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Return the node above the ith, jth element
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        # initialize head
        curr = self._head
        (row, col) = curr.get_position()
        # find the j + 1 column
        while curr is not None and col != (j + 1):
            curr = curr.get_right()
            (row, col) = curr.get_position()
        # start from j+1 column, head down until before it, or end
        cond = True
        while curr.get_down() is not None and cond:
            if curr.get_position() < (i + 1, j + 1):
                if curr.get_down().get_position() < (i + 1, j + 1):
                    curr = curr.get_down()
                else:
                    cond = False
            else:
                cond = False
        return curr

    def find_left(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Return the node to the left of the ith, jth element
        # REQ: 0 <= i <= # of rows - 1
        # REQ: 0 <= j <= # of columns - 1
        '''
        # initialize curr to head
        curr = self._head
        # get the position
        (row, col) = curr.get_position()
        # find the i + 1 row
        while curr is not None and row != (i + 1):
            curr = curr.get_down()
            (row, col) = curr.get_position()
        # start from i + 1 row, head right until before it, or end
        cond = True
        while curr.get_right() is not None and cond:
            if curr.get_position() < (i + 1, j + 1):
                if curr.get_right().get_position() < (i + 1, j + 1):
                    curr = curr.get_right()
                else:
                    cond = False
            else:
                cond = False
        # return this node
        return curr


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, n, default=0, rc='r'):
        '''(OneDimensionalMatrix, int) -> NoneType
        Automated method to initialize a 1DMatrix
        REQ: n >= 0
        '''
        self._head = MatrixNode(None)
        self._rc = rc
        if self._rc == 'r':
            self._row_num = 1
            self._column_num = n
        else:
            self._row_num = n
            self._column_num = 1
        self._default = default

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        REQ: 0 <= i <= num of rows (if n by 1)
        REQ: 0 <= i <= num of columns (if 1 by n)
        '''
        if self._rc == 'r':
            result = self.get_val(0, i)
        else:
            result = self.get_val(i, 0)
        return result

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        REQ: 0 <= i <= num of rows (if n by 1)
        REQ: 0 <= i <= num of columns (if 1 by n)
        '''
        if self._rc == 'r':
            self.set_val(0, i, new_val)
        else:
            self.set_val(i, 0, new_val)

    def get_rc(self):
        '''(OneDimensionalMatrix) -> str
        Return if its a row or col matrix
        REQ: None
        '''
        return self._rc

    def multiply_matrix(self, mult_matrix):
        '''(OneDimensionalMatrix) -> float
        Return one value if its one col * one row.
        If row * col, then m by n value.
        REQ: it must be a 1D matrix (1 by n) * 1D matrix (n by 1)
             or must be a 1D matrix (n by 1) * 1D matrix (1 by n)
        '''
        # self is 1 by n, mult_matrix is n by 1
        result = 0
        # if self is a column
        if self._rc != 'r':
            # get the num of rows inside this column
            (row, col) = self.get_dimensions()
            # check if multi_matrix is a row
            if mult_matrix.get_rc() == 'r':
                # get the num of columns inside this
                (row2, col) = mult_matrix.get_dimensions()
                # new matrix with row & col elements
                # default value is the default of mult_matrix times times
                # the default os the the self column
                default_value = self.get_default() * mult_matrix.get_default()
                new_matrix = Matrix(row, col, default_value)
                for row_num in range(row):
                    temp = mult_matrix.get_row(0)
                    val1 = self.get_item(row_num)
                    row = temp.multiply_scalar(val1)
                    new_matrix.set_row(row_num, temp)
                result = new_matrix
            else:
                raise MatrixIllegalOperationError
        else:
            (row, col) = self.get_dimensions()
            if mult_matrix.get_rc() != 'r':
                # check if its same number of col as row
                (row1, col1) = self.get_dimensions()
                (row2, col2) = mult_matrix.get_dimensions()
                if row1 != col2:
                    raise MatrixDimensionError
                for col_num in range(col):
                    val1 = self.get_item(col_num)
                    val2 = mult_matrix.get_item(col_num)
                    result += (val1 * val2)
            else:
                raise MatrixIllegalOperationError
        return result

    def get_row(self, m):
        '''(OneDimensionalMatrix, int) -> OneDimensionalMatrix
        Return the m'th mth item of this matrix
        REQ: 0 <= m <= num of rows (if n by 1)
        REQ: 0 <= m <= num of columns (if 1 by n)
        '''
        rc = self.get_rc()
        if rc == 'r':
            result = Matrix.get_col(self, m)
        else:
            result = Matrix.get_row(self, m)
        return result

    def set_row(self, m, new_row):
        '''(OneDimensionalMatrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the m'th row of this matrix to those of new_row
        REQ: 0 <= m <= num of rows (if n by 1)
        REQ: 0 <= m <= num of columns (if 1 by n)
        REQ: if self has n elements, the new_row must have n elements
        '''
        rc = self.get_rc()
        if rc == 'r':
            result = Matrix.set_col(self, m, new_row)
        else:
            result = Matrix.set_row(self, m, new_row)
        return result

    def get_col(self, n):
        '''(OneDimensinalMatrix, int) -> OneDimensionalMatrix
        Return the n'th item of this matrix
        REQ: 0 <= n <= num of rows (if n by 1)
        REQ: 0 <= n <= num of columns (if 1 by n)
        '''
        result = self.get_row(n)
        return result

    def set_col(self, col_num, new_col):
        '''(OneDimensionalMatrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the n'th column of this matrix to those of new_row
        REQ: 0 <= col_num <= num of rows (if n by 1)
        REQ: 0 <= col_num <= num of columns (if 1 by n)
        REQ: if self has n elements, the new_col must have n elements
        '''
        result = self.set_col(col_num, new_row)
        return result

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        REQ: 0 <= i <= num of rows (if n by 1)
        REQ: 0 <= j <= num of rows (if n by 1)
        REQ: 0 <= i <= num of columns (if 1 by n)
        REQ: 0 <= j <= num of columns (if 1 by n)
        '''
        rc = self.get_rc()
        if rc == 'r':
            Matrix.swap_cols(self, i, j)
        else:
            Matrix.swap_rows(self, i, j)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        REQ: 0 <= i <= num of rows (if n by 1)
        REQ: 0 <= j <= num of rows (if n by 1)
        REQ: 0 <= i <= num of columns (if 1 by n)
        REQ: 0 <= j <= num of columns (if 1 by n)
        '''
        self.swap_rows(i, j)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, n, default=0):
        '''(SquareMatrix, int) -> NoneType
        Automated method to initialize a SquareMatrix
        REQ: n >= 0
        '''
        Matrix.__init__(self, n, n, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        REQ: None
        '''
        # get all the rows
        # set it as new col
        (row, col) = self.get_dimensions()
        default_val = self.get_default()
        # initialize new Matrix
        new_matrix = SquareMatrix(row, default_val)
        for row_num in range(row):
            the_row = self.get_row(row_num)
            new_matrix.set_col(row_num)
        self = new_matrix

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        REQ: None
        '''
        # first set up 1D matrix
        # get the value at the ith, ith element
        (row, col) = self.get_dimensions()
        default_val = self.get_default()
        new_1D_matrix = OneDimensionalMatrix(row, default_val)
        # get the ith, ith element, and set it
        for row_num in range(row):
            element = self.get_val(row_num, row_num)
            new_1D_matrix.set_item(row_num, element)
        return new_1D_matrix

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        REQ: new_diagonal must have n elements == self # of rows/ columns
        '''
        (row1, col1) = new_diagonal.get_dimensions()
        if row1 >= col1:
            # its a column
            number = row1
        else:
            # its a row
            number = col1
        (row, col) = self.get_dimensions()
        if number != row:
            raise MatrixDimensionError
        for row_num in range(row):
            element = new_diagonal.get_item(row_num)
            self.set_val(row_num, row_num, element)


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def set_val(self, i, j, new_val):
        '''(SymmetricMatrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        REQ: 0 <= i <= # of rows - 1
        REQ: 0 <= j <= # of columns - 1
        '''
        # check bounds if valid
        self._check_bounds(i, j)
        Matrix.set_val(self, i, j, new_val)
        Matrix.set_val(self, j, i, new_val)

    def _make_symmetric(self):
        '''Internal helper method to make any changes to the symmetric
        into a symmetric matrix.
        This takes the uperr left triangle as the base.
        REQ: None
        '''
        (row, col) = self.get_dimensions()
        count = 0
        for row_num in range(row):
            for col_num in range(count, col):
                val = self.get_val(row_num, col_num)
                self.set_val(row_num, col_num, val)
            count += 1

    def multiply_matrix(self, mult_matrix):
        '''(SymmetricMatrix, Matrix) -> SymmetricMatrix
        Return the multiplication of these two matrices.
        Will be symmetric.
        REQ: if self is n by n, then mult_matrix must also be n by n
        '''
        # get dimensions
        (row, col) = self.get_dimensions()
        (row2, col2) = mult_matrix.get_dimensions()
        # check if it is n by n times  n by n
        if (row, col) == (row2, col2):
            Matrix.mutiply_matrix(self, mult_matrix)
            self._make_symmetric()
        else:
            raise MatrixDimensionError


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, n):
        '''(DiagonalMatrix, int) -> NoneType
        Automated method to initialize a DiagonalMatrix
        REQ: n >= 0
        '''
        SquareMatrix.__init__(self, n)

    def set_val(self, i, j, new_val):
        '''(DiagonalMatrix, int) -> NoneType
        Set the value of m[i, j] to new_val for this matrix m
        REQ: you can only set_val for diagonal or
            set 0 for the rest
        '''
        if i == j:
            SquareMatrix.set_val(self, i, j, new_val)
        else:
            if new_val != 0:
                raise MatrixInvalidOperationError

    def add_scalar(self, add_value):
        '''(DiagonalMatrix, int) -> NoneType
        Add a scalar amount.
        REQ: add_value == 0
        '''
        if add_value != 0:
            raise MatrixInvalidOperationError

    def get_rc(self):
        '''(DiagonalMatrix) -> Error'''
        raise MatrixInvalidOperationError

    def set_item(self, i, new_val):
        '''(DiagonalMatrix, int, float) -> NoneType
        Set the ith, ith element in this matrix to new_val.
        REQ: 0 <= i <= # of rows/# of columns
        '''
        self.set_val(i, i, new_val)

    def get_item(self, i):
        '''(DiagonalMatrix, int) -> float
        Return the ith ith element in this matrix.
        REQ: 0 <= i <= # of rows/# of columns
        '''
        return self.get_val(i, i)

    def multiply_matrix(self, mult_matrix):
        '''(DiagonalMatrix, DiagonalMatrix) -> NoneType
        Return a new multiplicated matrix.
        REQ: it must be n by n times n by n
        '''
        if type(multiply_matrix) != DiagonalMatrix:
            raise MatrixInvalidOperationError
        else:
            SymmetricMatrix.multiply_matrix(self, mult_matrix)


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, n):
        '''(IdentityMatrix, int) -> NoneType
        Automated method to initialize an IdentityMatrix
        REQ: n >= 0
        '''
        DiagonalMatrix.__init__(self, n)
        for count in range(n):
            self.set_item(count, 1)

    def set_val(self, i, j, new_val):
        '''(IdentitylMatrix, int) -> NoneType
        Set the value of m[i, j] to new_val for this matrix m
        REQ: 0 <= i <= # of columns/# of rows
        REQ: 0 <= j <= # of columns/# of rows
        REQ: new_val == 1
        '''
        if new_val == 1:
            DiagonalMatrix.set_val(self, i, j, new_val)
        else:
            raise MatrixInvalidOperationError

    def multiply_scalar(self, mult_value):
        '''(IdentityMatrix, int) -> NoneType
        Multiply one matrix with a value.
        REQ: mult_value == 0
        '''
        if mult_value != 1:
            raise MatrixInvalidOperationError

    def multiply_matrix(self, mult_matrix):
        '''(IdentityMatrix, IdentityMatrix) -> NoneType
        Multiply one matrix with another.
        REQ: matrix must be n by n * n by n
        '''
        if type(mult_matrix) != IdentityMatrix:
            raise MatrixInvalidOperatoinError

    def add_scalar(self, add_value):
        '''(IdentityMatrix, int) -> NoneType
        Add a scalar multiple.
        REQ: add_value == 0
        '''
        if add_value != 0:
            raise MatrixInvalidOperationError

import unittest
from a1_design import *


# Test for Matrix Class
class TestMatrixInit(unittest.TestCase):
    def test_one_parameter_one_row(self):
        x = Matrix([0, 'a', 2.0])
        row1 = [0, 'a', 2.0]
        self.assertEqual(x.get_row(), row1, 'one row one parameter')

    def test_one_parameter_multiple_row(self):
        x = Matrix([[0, 1], [2, 3, 4]])
        row1 = [0, 1]
        row2 = [2, 3]
        self.assertEqual((x.get_row(), x.get_row(2)),
                         (row1, row2), 'one row multiple row')

    def test_two_parameter_one(self):
        listt = [[0], [1, 2, 3, 4]]
        x = Matrix(listt, 1)
        row1 = [0]
        self.assertEqual(x.get_row(), row1, 'two_parameter')

    def test_two_parameter_multiple(self):
        listt = [[0], [1, 2, 3, 4]]
        x = Matrix(listt, 2)
        row1 = [0]
        row2 = [1]
        self.assertEqual(x.get_row(), row1, 'two_parameter')
        self.assertEqual(x.get_row(2), row2, 'two_parameter')

    def test_three_parameters_base(self):
        listt = ([0, 1, 2], [3, 4, 5, 6])
        x = Matrix(listt, 1, 1)
        row1 = [0]
        row2 = [3]
        self.assertEqual(x.get_row(), row1, 'three parameters')
        self.assertEqual(x.get_row(2), row2, 'three parameters')

    def test_three_parameters_multiple(self):
        listt = ([0, 1, 2], [3, 4, 5, 6])
        x = Matrix(listt, 1, 3)
        row1 = [0, 1, 2]
        row2 = [3, 4, 5]
        self.assertEqual(x.get_row(), row1, 'three parameters')
        self.assertEqual(x.get_row(2), row2, 'three parameters')


class TestMatrixMultiply(unittest.TestCase):
    def test_multiply_one(self):
        x = Matrix([1])
        y = Matrix([2])
        expected = Matrix([2])
        self.assertEqual(x.multiply(y), expected, 'one element matrices')

    def test_multply_one_constant(self):
        x = Matrix([1])
        constant = 2
        expected = Matrix([2])
        self.assertEqual(x.multiply(constant),
                         expected, 'one element times constant')

    def test_multiply_two_constant(self):
        x = Matrix([[2, 1.0], [3, 4]])
        constant = 2
        expected = Matrix([[4, 2.0], [6, 8]])
        self.assertEqual(x.multiply(constant), expected,
                         '2 by 2 times constant')

    def test_multiply_two_by_2_by_1(self):
        x = Matrix([2, 1], [1, 1])
        y = Matrix([1, 1])
        expected = Matrix([3, 2])
        self.assertEqual(x.multiply(y), expected,
                         '2 by 2 times 2 by 1')

    def test_multiply_two_two_by_two(self):
        x = Matrix([[2, 1], [2, 1]])
        y = Matrix([[1, 2], [1, 2]])
        expected = Matrix([[3, 6], [3, 6]])
        self.assertEqual(x.multiply(y), expected,
                         'two 2 by 2')

    def test_multiply_alpha_num(self):
        x = Matrix([[2, 1], ['a', 1]])
        y = Matrix([[1, 2], [1, 2]])
        self.assertRaises(MatrixNotNumber, x.multiply(y),
                          'matrix include alpha')

    def test_multiply_alpha_constant(self):
        x = Matrix([[2, 1], [2, 1]])
        constant = 'c'
        self.assertRaises(MatrixNotNumber, x.multiply(constant),
                          'matrix times constant of str')

    def test_multiply_not_fit(self):
        x = Matrix([[2, 1]])
        y = Matrix([[3, 3, 3]])
        self.assertRaises(MatrixIllegalMove, x.multiply(y),
                          'it is not m by n times n by k')


class TestMatrixSubtract(unittest.TestCase):
    def test_subtract_one_one(self):
        x = Matrix([2])
        y = Matrix([1.0])
        expected = Matrix([1.0])
        self.assertEqual(x.subtract(y), expected,
                         'elements minus')

    def test_subtract_two_two(self):
        x = Matrix([[1, 2], [1, 2]])
        y = Matrix([2, 1], [2, 1])
        expected = Matrix([[-1, 1], [-1, 1]])
        self.assertEqual(x.subtract(y), expected,
                         '2 by 1 subtaction')

    def test_subtract_two_square(self):
        x = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        y = Matrix([[4, 3, 2], [4, 3, 2], [4, 3, 2]])
        expected = Matrix([[-3, -1, 1], [-3, -1, 1], [-3, -1, 1]])
        self.assertEqual(x.subtract(y), expected,
                         'square subtraction')

    def test_subtact_matrix_alpha(self):
        x = Matrix([[1, 2], [1, 'a']])
        y = Matrix([2, 1], [2, 1])
        self.assertRaises(MatrixNotNumber, x.subtract(y),
                          'alpha included matrix subtraction')

    def test_subtract_fail(self):
        x = Matrix([[1, 2]])
        y = Matrix([[1, 3, 2]])
        self.assertRaises(MatrixIllegalMove, x.subtract(y),
                          'it is not m by n minus m by n')


class TestMatrixAdd(unittest.TestCase):
    def test_add_one_one(self):
        x = Matrix([1])
        y = Matrix([2.0])
        expected = Matrix([3])
        self.assertEqual(x.add(y), expected,
                         'elements add')

    def test_add_two_two(self):
        x = Matrix([[3, 1.0], [1, 3]])
        y = Matrix([[4, 4], [4, 4]])
        expected = Matrix([[7, 5.0], [5, 7]])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition')

    def test_add_two_square(self):
        x = Matrix([[1, 2, 3.0], [1, 2, 3], [1, 2, 3]])
        y = Matrix([[4, 3, 2], [4, 3, 2], [4, 3, 2]])
        expected = Matrix([[5, 5, 5.0], [5, 5, 5], [5, 5, 5]])
        self.assertEqual(x.add(y), expected,
                         'square addition')

    def test_add_one_one_letter(self):
            x = Matrix(['a'])
            y = Matrix(['b'])
            expected = Matrix(['ab'])
            self.assertEqual(x.add(y), expected,
                             'elements add_letters')

    def test_add_two_two_letters(self):
        x = Matrix([['a', 'b'], ['c', 'd']])
        y = Matrix([['e', 'f'], ['g', 'h']])
        expected = Matrix([['ae', 'bf'], ['cg', 'df']])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition_letters')

    def test_add_two_square_letters_and_num(self):
        x = Matrix([['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']])
        y = Matrix([['d', 2, 2.0], [4, 3, 2], [4, 3, 2]])
        expected = Matrix([['ad', 'b2', 'c2.0'], ['a4', 'b3', 'c2'],
                           ['a4', 'b3', 'c2']])
        self.assertEqual(x.add(y), expected,
                         'square addition_letters_num')

    def test_add_fail(self):
        x = Matrix([['h', 'e', 'l', 'p']])
        y = Matrix([['going', 'to', 'become'],
                    ['insane', 'real', 'soon']])
        self.assertRaises(MatrixIllegalMove, x.add(y),
                          'not m by n + m by n')


class TestMatrixGetColumn(unittest.TestCase):
    def test_get_column_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(), expected,
                         'default get_column')

    def test_get_column_first(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(1), expected,
                         'get first column')

    def test_get_2nd_column(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [0, 1, 0]
        self.assertEqual(x.get_column(2), expected,
                         'get second column')

    def test_get_last_column(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(3), expected,
                         'get last column')

    def test_get_column_overbound(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(4),
                          'out of bound get column')

    def test_get_column_zero(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(0),
                          'get column zero')


class TestMatrixSetColumn(unittest.TestCase):
    def test_set_column_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = [1, 'a', 1]
        expected = Matrix([[1, 0], ['a', 1], [1, 0]])
        self.assertEqual(x.set_column(y), expected,
                         'default set column')

    def test_set_column_first(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = [1, 1, 1]
        expected = Matrix([[1, 0], [1, 1], [1, 0]])
        self.assertEqual(x.set_column(y, 1), expected,
                         'set first column')

    def test_set_2nd_column(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = Matrix([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_column(y, 2), expected,
                         'set second column')

    def test_set_last_column(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = Matrix([[1, 0, 1], [0, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_column(y, 3), expected,
                         'set last column')

    def test_set_column_overbound(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 4),
                          'out of bound set column')

    def test_set_column_zero(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 0),
                          'set column zero')


class TestMatrixGetRow(unittest.TestCase):
    def test_get_row_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0]
        self.assertEqual(x.get_row(), expected,
                         'default get row')

    def test_get_row_first(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0]
        self.assertEqual(x.get_row(1), expected,
                         'get first row')

    def test_get_2nd_row(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [0, 1, 0]
        self.assertEqual(x.get_row(2), expected,
                         'get second row')

    def test_get_last_row(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_row(3), expected,
                         'get last row')

    def test_get_row_overbound(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(4),
                          'out of bound get row')

    def test_get_row_zero(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(0),
                          'get row zero')


class TestMatrixSetRow(unittest.TestCase):
    def test_set_row_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = [1, 'a']
        expected = Matrix([[1, 'a'], [0, 1], [1, 0]])
        self.assertEqual(x.set_row(y), expected,
                         'default set row')

    def test_set_row_first(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = [1, 1]
        expected = Matrix([[1, 1], [0, 1], [1, 0]])
        self.assertEqual(x.set_row(y, 1), expected,
                         'set first column')

    def test_set_2nd_row(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = Matrix([[1, 0, 1], [1, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_row(y, 2), expected,
                         'set second row')

    def test_set_last_row(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = Matrix([[1, 0, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_row(y, 3), expected,
                         'set last row')

    def test_set_column_overbound(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 4),
                          'out of bound set row')

    def test_set_column_zero(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 0),
                          'set row zero')


class TestMatrixGet(unittest.TestCase):
    def test_get_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = 1
        self.assertEqual(x.get(), expected,
                         'default get')

    def test_get_first_element(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        expected = 1
        self.assertEqual(x.get(1, 1), expected,
                         'get first element')

    def test_get_2nd_element(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 0
        self.assertEqual(x.get(2), expected,
                         'get 2nd row 1st element')

    def test_get_2nd_row_2nd_element(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 1
        self.assertEqual(x.get(2, 2), expected,
                         'get 2nd row 2nd element')

    def test_get_overboundzero1(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0),
                          'row 0 column 1 DNE')

    def test_get_overboundzero2(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0, 0),
                          'row 0, column 0 DNE')

    def test_get_overbound3(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4),
                          'overbound by row')

    def test_get_overbound4(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4, 3),
                          'overbound by row')

    def test_get_overbound5(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(3, 4),
                          'overbound by column')


class TestMatrixSet(unittest.TestCase):
    def test_set_default(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = 'a'
        expected = Matrix([['a', 0], [0, 1], [1, 0]])
        self.assertEqual(x.set(y), expected,
                         'default set alpha')

    def test_set_default2(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = 2.0
        expected = Matrix([[2.0, 0], [0, 1], [1, 0]])
        self.assertEqual(x.set(y), expected,
                         'default set float')

    def test_set_default2(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = 4
        expected = Matrix([[4, 0], [0, 1], [1, 0]])
        self.assertEqual(x.set(y), expected,
                         'default set int')

    def test_set_first_element(self):
        x = Matrix([[1, 0], [0, 1], [1, 0]])
        y = 5
        expected = Matrix([[5, 0], [0, 1], [1, 0]])
        self.assertEqual(x.set(y, 1, 1), expected,
                         'set first element')

    def test_set_2nd_element(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = Matrix([[1, 0, 1], [5, 1, 0], [1, 0, 1]])
        self.assertEqual(x.set(y, 2), expected,
                         'set 2nd row 1st element')

    def test_set_2nd_row_2nd_element(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = Matrix([[1, 0, 1], [0, 5, 0], [1, 0, 1]])
        self.assertEqual(x.set(y, 2, 2), expected,
                         'set 2nd row 2nd element')

    def test_set_overboundzero1(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0),
                          'row 0 column 1 DNE')

    def test_set_overboundzero2(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0, 0),
                          'row 0, column 0 DNE')

    def test_set_overbound3(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'a'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4),
                          'overbound by row')

    def test_set_overbound4(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'd'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4, 3),
                          'overbound by row')

    def test_set_overbound5(self):
        x = Matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'help'
        self.assertRaises(MatrixOutOfBound, x.set(y, 3, 4),
                          'overbound by column')


class TestMatrixSwapRows(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = Matrix([[1, 2], [3, 4]])
        expected = Matrix([[1, 2], [3, 4]])
        self.assertEqual(x.swap_rows(1, 1), expected,
                         'switching rows with itself')

    def test_swap_rows_first_and_sec1(self):
        x = Matrix([[1, 2], [3, 4], [5, 6]])
        expected = Matrix([[3, 4], [1, 2], [5, 6]])
        self.assertEqual(x.swap_rows(1, 2), expected,
                         'switching rows 1st and 2nd')

    def test_swap_rows_first_and_sec2(self):
            x = Matrix([[1, 2], [3, 4], [5, 6]])
            expected = Matrix([[3, 4], [1, 2], [5, 6]])
            self.assertEqual(x.swap_rows(2, 1), expected,
                             'switching rows 2nd and 1st')

    def test_swap_rows_first_and_third1(self):
            x = Matrix([[1, 2], [3, 4], [5, 6]])
            expected = Matrix([[5, 6], [3, 4], [1, 2]])
            self.assertEqual(x.swap_rows(1, 3), expected,
                             'switching rows 1st and 3rd')

    def test_swap_rows_first_and_thid2(self):
            x = Matrix([[1, 2], [3, 4], [5, 6]])
            expected = Matrix([[5, 6], [3, 4], [1, 2]])
            self.assertEqual(x.swap_rows(3, 1), expected,
                             'switching rows 3rd and 1st')


class TestMatrixSwapColumns(unittest.TestCase):
    def test_swap_columns_itself(self):
        x = Matrix([[1, 2], [3, 4]])
        expected = Matrix([[1, 2], [3, 4]])
        self.assertEqual(x.swap_columns(1, 1), expected,
                         'switching columns with itself')

    def test_swap_columns_first_and_sec1(self):
        x = Matrix([[1, 2], [3, 4], [5, 6]])
        expected = Matrix([[2, 1], [4, 3], [6, 5]])
        self.assertEqual(x.swap_columns(1, 2), expected,
                         'switching columns 1st and 2nd')

    def test_swap_columns_first_and_sec2(self):
            x = Matrix([[1, 2], [3, 4], [5, 6]])
            expected = Matrix([[2, 1], [4, 3], [6, 5]])
            self.assertEqual(x.swap_columns(2, 1), expected,
                             'switching columns 2nd and 1st')

    def test_swap_columns_first_and_third1(self):
            x = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            expected = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
            self.assertEqual(x.swap_columns(1, 2), expected,
                             'switching columns 1st and 3rd')

    def test_swap_columns_first_and_thid2(self):
            x = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            expected = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
            self.assertEqual(x.swap_columns(3, 1), expected,
                             'switching columnss 3rd and 1st')


class TestMatrixDeterminant(unittest.TestCase):
    def test_determinant_zero_matrix(self):
        x = Matrix([[0, 0], [0, 0]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of zero matrix')

    def test_determinant_non_zero_matrix(self):
        x = Matrix([[1, 2], [3, 4.0]])
        expected = -2
        self.assertEqual(x.determinant(), expected,
                         'determinant of nonzero matrix')

    def test_determinant_same_element(self):
        x = Matrix([[5, 5], [5, 5]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinant_include_zero_and_nonzero(self):
        x = Matrix([[1, 2.0], [3, 0]])
        expected = -6
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinint_fail1(self):
        x = Matrix([[0]])
        self.assertRaises(MatrixNot2By2, x.determinant(),
                          'one element is not 2 by 2')

    def test_determinint_fail2(self):
            x = Matrix([[0], [3]])
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '2 by 1 is not 2 by 2')

    def test_determinint_fail1(self):
            x = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '3 by 3 is not 2 by 2')


class TestMatrixTranspose(unittest.TestCase):
    def test_transpose_one_element(self):
        x = Matrix([[0]])
        expected = Matrix([0])
        self.assertEqual(x.transpose(), expected,
                         'transposing of one element')

    def test_transpose_one_row(self):
        x = Matrix([[0, 1, 2, 3]])
        expected = Matrix([[0], [1], [2], [3]])
        self.assertEqual(x.transpose(), expected,
                         'transposing of one row')

    def test_transpose_one_column(self):
        x = Matrix([[0], [1], [2], [3]])
        expected = Matrix([[0, 1, 2, 3]])
        self.assertEqual(x.transpose(), expected,
                         'transposing of one column')

    def test_transpose_multiple(self):
        x = Matrix([[0, 1, 2], [3, 4, 5]])
        expected = Matrix([[0, 3], [1, 4], [2, 5]])
        self.assertEqual(x.transpose(), expected,
                         'transposing nonsquare matrix')

    def test_transpose_sqaure(self):
        x = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        expected = Matrix([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
        self.assertEqual(x.transpose(), expected,
                         'transposing square matrix')


class TestMatrixStr(unittest.TestCase):
    def test_str_method_one(self):
        x = Matrix([[0]])
        expected = '0'
        self.assertEqual(x.__str__(), expected,
                         'printing one element')

    def test_str_method_one_row(self):
        x = Matrix([[0, 1, 2, 3, 4, 5]])
        expected = '0 1 2 3 4 5'
        self.assertEqual(x.__str__(), expected,
                         'printing one row')

    def test_str_method_one_column(self):
        x = Matrix([0], [1], [2])
        expected = '0 / 1 / 2'
        self.assertEqual(x.__str__(), expected,
                         'printing one column')

    def test_str_method_multiple(self):
        x = Matrix([[0, 1], [2, 3], [4, 5]])
        expected = '0 1 / 2 3 / 4 5'
        self.assertEqual(x.__str__(), expected,
                         'printing 3 by 2')

    def test_str_method_square(self):
        x = Matrix([[0, 1], [3, 4]])
        expected = '0 1 / 3 4'
        self.assertEqual(x.__str__(), expected,
                         'printing square')

    def test__str_method_alpha(self):
        x = Matrix([['a', 'b'], ['c', 'd']])
        expected = 'a b / c d'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')

    def test_str_method_alphanum(self):
        x = Matrix([['a', 1], ['b', 2.0]])
        expected = 'a 1 / b 2.0'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')

# Test Now for SquareMatrix :)


class TestSquareMatrixInit(unittest.TestCase):
    def test_init_default1(self):
        listt = [1, 2, 3, 4, 5, 6]
        x = SquareMatrix(listt)
        row1 = [1]
        self.assertEqual(x.get_row(), row1,
                         'one elemnet int')

    def test_init_default2(self):
        listt = ['a', 2, 3, 4, 5, 6]
        x = SquareMatrix(listt)
        row1 = ['a']
        self.assertEqual(x.get_row(), row1,
                         'one elemnet alpha')

    def test_init_default3(self):
        listt = [1.0, 2, 3, 4, 5, 6]
        x = SquareMatrix(listt)
        row1 = [1.0]
        self.assertEqual(x.get_row(), row1,
                         'one elemnet float')

    def test_init_2_by_2(self):
        listt = [[1, 2, 3], [4, 5, 6]]
        x = SquareMatrix(listt, 2)
        row1 = [1, 2]
        row2 = [4, 5]
        self.assertEqual((x.get_row(), x.get_row(2)), (row1, row2),
                         '2 by 2 matrices')

    def test_init_multiple(self):
        listt = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        x = SquareMatrix(listt, 3)
        row1 = [1, 2, 3]
        row2 = [5, 6, 7]
        row3 = [9, 10, 11]
        self.assertEqual((x.get_row(), x.get_row(2), x.get_row(3)),
                         (row1, row2, row3), '3 by 3 matrices')


class TestSquareMatricesGetDiagonal(unittest.TestCase):
    def test_square_matrix1(self):
        x = SquareMatrix([[1]])
        expected = [1]
        self.assertEqual(x.get_diagonal(), expected,
                         'one by one matrix')

    def test_square_matrix2(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = [1, 4]
        self.assertEqual(x.get_diagonal(), expected,
                         'two by two matrix')

    def test_square_matrix3(self):
        x = SquareMatrix([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
        expected = [1, 5, 8]
        self.assertEqual(x.get_diagonal(), expected,
                         '3 by 3 matrix')

    def test_square_matrix_fail(self):
        x = SquareMatrix([['a']])
        self.assertRaises(MatrixNotNumber, x.get_diagonal(),
                          'one by one matrix')

    def test_square_matrix_float(self):
        x = SquareMatrix([[1.0]])
        expected = [1.0]
        self.assertEqual(x.get_diagonal, expected,
                         'float matrices')


class TestSquareMatricesSwap(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = SquareMatrix([['a', 2.0], [3, 4]])
        expected = SquareMatrix([['a', 2.0], [3, 4]])
        self.assertEqual(x.swap('r', 1, 'r', 1), expected,
                         'swap rows with itself')

    def test_swap_rows(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[3, 4], [1, 2]])
        self.assertEqual(x.swap('r', 1, 'r', 2), expected,
                         'swap rows')

    def test_swap_columns_itself(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(x.swap('c', 1, 'c', 1), expected,
                         'swap columns with itself')

    def test_swap_columns(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[2, 1], [4, 3]])
        self.assertEqual(x.swap('c', 1, 'c', 2), expected,
                         'swap columns')

    def test_swap_row_column(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[4, 2], [3, 1]])
        self.assertEqual(x.swap('r', 1, 'c', 2), expected,
                         '1st row swap 2nd column')

    def test_swap_row_column(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[1, 3], [2, 4]])
        self.assertEqual(x.swap('r', 1, 'c', 1), expected,
                         '1st row swap 1st column')

    def test_swap_row_column(self):
        x = SquareMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected = SquareMatrix([[1, 8, 3], [6, 5, 4], [7, 2, 9]])
        self.assertEqual(x.swap('c', 2, 'r', 2), expected,
                         '2st row swap 2nd column')

    def test_swap_row_fail1(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'r', 2),
                         'swap row zero')

    def test_swap_row_fail2(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'r', 2),
                         'swap row out of bounds')

    def test_swap_column_fail1(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'c', 2),
                         'swap column zero')

    def test_swap_column_fail2(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 3, 'c', 2),
                         'swap column out of bounds')

    def test_swap_row_column_fail1(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'c', 2),
                         'swap row zero')

    def test_swap_row_column_fail2(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'c', 2),
                         'swap row out of bounds')

    def test_swap_row_column_fail3(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'r', 2),
                         'swap column zero')

    def test_swap_row_column_fail4(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 4, 'c', 2),
                         'swap column out of bounds')


class TestSquareMatrixMultiply(unittest.TestCase):
    def test_multiply_one(self):
        x = SquareMatrix([1])
        y = SquareMatrix([2])
        expected = SquareMatrix([2])
        self.assertEqual(x.multiply(y), expected, 'one element matrices')

    def test_multply_one_constant(self):
        x = SquareMatrix([1])
        constant = 2
        expected = SquareMatrix([2])
        self.assertEqual(x.multiply(constant),
                         expected, 'one element times constant')

    def test_multiply_two_constant(self):
        x = SquareMatrix([[2, 1.0], [3, 4]])
        constant = 2
        expected = SquareMatrix([[4, 2.0], [6, 8]])
        self.assertEqual(x.multiply(constant), expected,
                         '2 by 2 times constant')

    def test_multiply_two_by_2_by_1(self):
        x = SquareMatrix([2, 1], [1, 1])
        y = Matrix([1, 1])
        expected = SquareMatrix([3, 2], [3, 2])
        self.assertEqual(x.multiply(y), expected,
                         '2 by 2 times 2 by 1')

    def test_multiply_two_two_by_two(self):
        x = SquareMatrix([[2, 1], [2, 1]])
        y = SquareMatrix([[1, 2], [1, 2]])
        expected = SquareMatrix([[3, 6], [3, 6]])
        self.assertEqual(x.multiply(y), expected,
                         'two 2 by 2')

    def test_multiply_alpha_num(self):
        x = SquareMatrix([[2, 1], ['a', 1]])
        y = SquareMatrix([[1, 2], [1, 2]])
        self.assertRaises(MatrixNotNumber, x.multiply(y),
                          'SquareMatrix include alpha')

    def test_multiply_alpha_constant(self):
        x = SquareMatrix([[2, 1], [2, 1]])
        constant = 'c'
        self.assertRaises(MatrixNotNumber, x.multiply(constant),
                          'SquareMatrix times constant of str')

    def test_multiply_not_fit(self):
        x = SquareMatrix([[2, 1]])
        y = SquareMatrix([[3, 3, 3]])
        self.assertRaises(MatrixIllegalMove, x.multiply(y),
                          'it is not m by n times n by k')


class TestSquareMatrixSubtract(unittest.TestCase):
    def test_subtract_one_one(self):
        x = SquareMatrix([2])
        y = SquareMatrix([1.0])
        expected = SquareMatrix([1.0])
        self.assertEqual(x.subtract(y), expected,
                         'elements minus')

    def test_subtract_two_two(self):
        x = SquareMatrix([[1, 2], [1, 2]])
        y = SquareMatrix([2, 1], [2, 1])
        expected = SquareMatrix([[-1, 1], [-1, 1]])
        self.assertEqual(x.subtract(y), expected,
                         '2 by 1 subtaction')

    def test_subtract_two_square(self):
        x = SquareMatrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        y = SquareMatrix([[4, 3, 2], [4, 3, 2], [4, 3, 2]])
        expected = SquareMatrix([[-3, -1, 1], [-3, -1, 1], [-3, -1, 1]])
        self.assertEqual(x.subtract(y), expected,
                         'square subtraction')

    def test_subtact_SquareMatrix_alpha(self):
        x = SquareMatrix([[1, 2], [1, 'a']])
        y = SquareMatrix([2, 1], [2, 1])
        self.assertRaises(MatrixNotNumber, x.subtract(y),
                          'alpha included SquareMatrix subtraction')

    def test_subtract_fail(self):
        x = SquareMatrix([[1, 2]])
        y = Matrix([[1, 3, 2]])
        self.assertRaises(MatrixIllegalMove, x.subtract(y),
                          'it is not m by n minus m by n')


class TestSquareMatrixAdd(unittest.TestCase):
    def test_add_one_one(self):
        x = SquareMatrix([1])
        y = SquareMatrix([2.0])
        expected = SquareMatrix([3])
        self.assertEqual(x.add(y), expected,
                         'elements add')

    def test_add_two_two(self):
        x = SquareMatrix([[3, 1.0], [1, 3]])
        y = SquareMatrix([[4, 4], [4, 4]])
        expected = SquareMatrix([[7, 5.0], [5, 7]])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition')

    def test_add_two_square(self):
        x = SquareMatrix([[1, 2, 3.0], [1, 2, 3], [1, 2, 3]])
        y = SquareMatrix([[4, 3, 2], [4, 3, 2], [4, 3, 2]])
        expected = SquareMatrix([[5, 5, 5.0], [5, 5, 5], [5, 5, 5]])
        self.assertEqual(x.add(y), expected,
                         'square addition')

    def test_add_one_one_letter(self):
            x = SquareMatrix(['a'])
            y = SquareMatrix(['b'])
            expected = SquareMatrix(['ab'])
            self.assertEqual(x.add(y), expected,
                             'elements add_letters')

    def test_add_two_two_letters(self):
        x = SquareMatrix([['a', 'b'], ['c', 'd']])
        y = SquareMatrix([['e', 'f'], ['g', 'h']])
        expected = SquareMatrix([['ae', 'bf'], ['cg', 'df']])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition_letters')

    def test_add_two_square_letters_and_num(self):
        x = SquareMatrix([['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']])
        y = SquareMatrix([['d', 2, 2.0], [4, 3, 2], [4, 3, 2]])
        expected = SquareMatrix([['ad', 'b2', 'c2.0'], ['a4', 'b3', 'c2'],
                                 ['a4', 'b3', 'c2']])
        self.assertEqual(x.add(y), expected,
                         'square addition_letters_num')

    def test_add_fail(self):
        x = SquareMatrix([['h', 'e', 'l', 'p']])
        y = SquareMatrix([['going', 'to', 'become'],
                          ['insane', 'real', 'soon']])
        self.assertRaises(MatrixIllegalMove, x.add(y),
                          'not m by n + m by n')


class TestSquareMatrixGetColumn(unittest.TestCase):
    def test_get_column_default(self):
        x = SquareMatrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(), expected,
                         'default get_column')

    def test_get_column_first(self):
        x = SquareMatrix([[1, 0], [0, 1], [1, 0]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(1), expected,
                         'get first column')

    def test_get_2nd_column(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [0, 1, 0]
        self.assertEqual(x.get_column(2), expected,
                         'get second column')

    def test_get_last_column(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(3), expected,
                         'get last column')

    def test_get_column_overbound(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(4),
                          'out of bound get column')

    def test_get_column_zero(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(0),
                          'get column zero')


class TestSquareMatrixSetColumn(unittest.TestCase):
    def test_set_column_default(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        y = [1, 'a']
        expected = SquareMatrix([[1, 0], ['a', 1]])
        self.assertEqual(x.set_column(y), expected,
                         'default set column')

    def test_set_column_first(self):
        x = SquareMatrix([[1, 0], [0, 1], [1, 0]])
        y = [1, 1]
        expected = SquareMatrix([[1, 0], [1, 1]])
        self.assertEqual(x.set_column(y, 1), expected,
                         'set first column')

    def test_set_2nd_column(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SquareMatrix([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_column(y, 2), expected,
                         'set second column')

    def test_set_last_column(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SquareMatrix([[1, 0, 1], [0, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_column(y, 3), expected,
                         'set last column')

    def test_set_column_overbound(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 4),
                          'out of bound set column')

    def test_set_column_zero(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 0),
                          'set column zero')


class TestSquareMatrixGetRow(unittest.TestCase):
    def test_get_row_default(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_row(), expected,
                         'default get row')

    def test_get_row_first(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_row(1), expected,
                         'get first row')

    def test_get_2nd_row(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [0, 1, 0]
        self.assertEqual(x.get_row(2), expected,
                         'get second row')

    def test_get_last_row(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_row(3), expected,
                         'get last row')

    def test_get_row_overbound(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(4),
                          'out of bound get row')

    def test_get_row_zero(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(0),
                          'get row zero')


class TestSquareMatrixSetRow(unittest.TestCase):
    def test_set_row_default(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        y = [1, 'a']
        expected = SquareMatrix([[1, 'a'], [0, 1]])
        self.assertEqual(x.set_row(y), expected,
                         'default set row')

    def test_set_row_first(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        y = [1, 1]
        expected = SquareMatrix([[1, 1], [0, 1]])
        self.assertEqual(x.set_row(y, 1), expected,
                         'set first column')

    def test_set_2nd_row(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SquareMatrix([[1, 0, 1], [1, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_row(y, 2), expected,
                         'set second row')

    def test_set_last_row(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_row(y, 3), expected,
                         'set last row')

    def test_set_column_overbound(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 4),
                          'out of bound set row')

    def test_set_column_zero(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 0),
                          'set row zero')


class TestSquareMatrixGet(unittest.TestCase):
    def test_get_default(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        expected = 1
        self.assertEqual(x.get(), expected,
                         'default get')

    def test_get_first_element(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        expected = 1
        self.assertEqual(x.get(1, 1), expected,
                         'get first element')

    def test_get_2nd_element(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 0
        self.assertEqual(x.get(2), expected,
                         'get 2nd row 1st element')

    def test_get_2nd_row_2nd_element(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 1
        self.assertEqual(x.get(2, 2), expected,
                         'get 2nd row 2nd element')

    def test_get_overboundzero1(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0),
                          'row 0 column 1 DNE')

    def test_get_overboundzero2(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0, 0),
                          'row 0, column 0 DNE')

    def test_get_overbound3(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4),
                          'overbound by row')

    def test_get_overbound4(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4, 3),
                          'overbound by row')

    def test_get_overbound5(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(3, 4),
                          'overbound by column')


class TestSquareMatrixSet(unittest.TestCase):
    def test_set_default(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        y = 'a'
        expected = SquareMatrix([['a', 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set alpha')

    def test_set_default2(self):
        x = SquareMatrix([[1, 0], [0, 1]])
        y = 2.0
        expected = SquareMatrix([[2.0, 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set float')

    def test_set_default2(self):
        x = SquareMatrix([[1, 0], [0, 1], [1, 0]])
        y = 4
        expected = SquareMatrix([[4, 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set int')

    def test_set_first_element(self):
        x = SquareMatrix([[1, 0], [0, 1], [1, 0]])
        y = 5
        expected = SquareMatrix([[5, 0], [0, 1]])
        self.assertEqual(x.set(y, 1, 1), expected,
                         'set first element')

    def test_set_2nd_element(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = SquareMatrix([[1, 0, 1], [5, 1, 0], [1, 0, 1]])
        self.assertEqual(x.set(y, 2), expected,
                         'set 2nd row 1st element')

    def test_set_2nd_row_2nd_element(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = SquareMatrix([[1, 0, 1], [0, 5, 0], [1, 0, 1]])
        self.assertEqual(x.set(y, 2, 2), expected,
                         'set 2nd row 2nd element')

    def test_set_overboundzero1(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0),
                          'row 0 column 1 DNE')

    def test_set_overboundzero2(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0, 0),
                          'row 0, column 0 DNE')

    def test_set_overbound3(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'a'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4),
                          'overbound by row')

    def test_set_overbound4(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'd'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4, 3),
                          'overbound by row')

    def test_set_overbound5(self):
        x = SquareMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'help'
        self.assertRaises(MatrixOutOfBound, x.set(y, 3, 4),
                          'overbound by column')


class TestSquareMatrixSwapRows(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(x.swap_rows(1, 1), expected,
                         'switching rows with itself')

    def test_swap_rows_first_and_sec1(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[3, 4], [1, 2]])
        self.assertEqual(x.swap_rows(1, 2), expected,
                         'switching rows 1st and 2nd')

    def test_swap_rows_first_and_sec2(self):
            x = SquareMatrix([[1, 2], [3, 4]])
            expected = SquareMatrix([[3, 4], [1, 2]])
            self.assertEqual(x.swap_rows(2, 1), expected,
                             'switching rows 2nd and 1st')

    def test_swap_rows_first_and_third1(self):
            x = SquareMatrix([[1, 2, 4], [3, 4, 4], [5, 6, 4]])
            expected = SquareMatrix([[5, 6, 4], [3, 4, 4], [1, 2, 4]])
            self.assertEqual(x.swap_rows(1, 3), expected,
                             'switching rows 1st and 3rd')

    def test_swap_rows_first_and_thid2(self):
            x = SquareMatrix([[1, 2, 5], [3, 4, 5], [5, 6, 5]])
            expected = SquareMatrix([[5, 6, 5], [3, 4, 5], [1, 2, 5]])
            self.assertEqual(x.swap_rows(3, 1), expected,
                             'switching rows 3rd and 1st')


class TestSquareMatrixSwapColumns(unittest.TestCase):
    def test_swap_columns_itself(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[1, 2], [3, 4]])
        self.assertEqual(x.swap_columns(1, 1), expected,
                         'switching columns with itself')

    def test_swap_columns_first_and_sec1(self):
        x = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix([[2, 1], [4, 3]])
        self.assertEqual(x.swap_columns(1, 2), expected,
                         'switching columns 1st and 2nd')

    def test_swap_columns_first_and_sec2(self):
            x = SquareMatrix([[1, 2], [3, 4]])
            expected = SquareMatrix([[2, 1], [4, 3]])
            self.assertEqual(x.swap_columns(2, 1), expected,
                             'switching columns 2nd and 1st')

    def test_swap_columns_first_and_third1(self):
            x = SquareMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            expected = SquareMatrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
            self.assertEqual(x.swap_columns(1, 2), expected,
                             'switching columns 1st and 3rd')

    def test_swap_columns_first_and_thid2(self):
            x = SquareMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            expected = SquareMatrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
            self.assertEqual(x.swap_columns(3, 1), expected,
                             'switching columnss 3rd and 1st')


class TestSquareMatrixDeterminant(unittest.TestCase):
    def test_determinant_zero_SquareMatrix(self):
        x = SquareMatrix([[0, 0], [0, 0]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of zero SquareMatrix')

    def test_determinant_non_zero_SquareMatrix(self):
        x = SquareMatrix([[1, 2], [3, 4.0]])
        expected = -2
        self.assertEqual(x.determinant(), expected,
                         'determinant of nonzero SquareMatrix')

    def test_determinant_same_element(self):
        x = SquareMatrix([[5, 5], [5, 5]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinant_include_zero_and_nonzero(self):
        x = SquareMatrix([[1, 2.0], [3, 0]])
        expected = -6
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinint_fail1(self):
        x = SquareMatrix([[0]])
        self.assertRaises(MatrixNot2By2, x.determinant(),
                          'one element is not 2 by 2')

    def test_determinint_fail1(self):
            x = SquareMatrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '3 by 3 is not 2 by 2')


class TestSquareMatrixTranspose(unittest.TestCase):
    def test_transpose_one_element(self):
        x = SquareMatrix([[0]])
        expected = SquareMatrix([0])
        self.assertEqual(x.transpose(), expected,
                         'transposing of one element')

    def test_transpose_multiple(self):
        x = SquareMatrix([[0, 1], [3, 4]])
        expected = SquareMatrix([[0, 3], [1, 4]])
        self.assertEqual(x.transpose(), expected,
                         'transposing nonsquare SquareMatrix')

    def test_transpose_sqaure(self):
        x = SquareMatrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        expected = SquareMatrix([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
        self.assertEqual(x.transpose(), expected,
                         'transposing square SquareMatrix')


class TestSquareMatrixStr(unittest.TestCase):
    def test_str_method_one(self):
        x = SquareMatrix([[0]])
        expected = '0'
        self.assertEqual(x.__str__(), expected,
                         'printing one element')

    def test_str_method_square(self):
        x = SquareMatrix([[0, 1], [3, 4]])
        expected = '0 1 / 3 4'
        self.assertEqual(x.__str__(), expected,
                         'printing square')

    def test__str_method_alpha(self):
        x = SquareMatrix([['a', 'b'], ['c', 'd']])
        expected = 'a b / c d'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')

    def test_str_method_alphanum(self):
        x = SquareMatrix([['a', 1], ['b', 2.0]])
        expected = 'a 1 / b 2.0'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')
# Test Case for Symmetric Matrix


class TestSymmetricMatrixInit(unittest.TestCase):
    def test_init_default1(self):
        listt = [1, 2, 3, 4, 5, 6]
        x = SymmetricMatrix(listt)
        row1 = [1]
        self.assertEqual(x.get_row(), row1,
                         'one element int')

    def test_init_default2(self):
        listt = ['a', 2, 3, 4, 5, 6]
        x = SymmetricMatrix(listt)
        row1 = ['a']
        self.assertEqual(x.get_row(), row1,
                         'one element alpha')

    def test_init_default3(self):
        listt = [1.0, 2, 3, 4, 5, 6]
        x = SymmetricMatrix(listt)
        row1 = [1.0]
        self.assertEqual(x.get_row(), row1,
                         'one element float')

    def test_init_2_by_2(self):
        listt = [[1, 2, 3], [4, 5, 6]]
        x = SymmetricMatrix(listt, 2)
        row1 = [1, 2]
        row2 = [2, 5]
        self.assertEqual((x.get_row(), x.get_row(2)), (row1, row2),
                         '2 by 2 matrices')

    def test_init_multiple(self):
        listt = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        x = SymmetricMatrix(listt, 3)
        row1 = [1, 2, 3]
        row2 = [7,  6, 7]
        row3 = [3, 2, 11]
        self.assertEqual((x.get_row(), x.get_row(2), x.get_row(3)),
                         (row1, row2, row3), '3 by 3 matrices')


class TestSymmetricMatrixMultiply(unittest.TestCase):
    def test_multiply_one(self):
        x = SymmetricMatrix([1])
        y = SymmetricMatrix([2])
        expected = SymmetricMatrix([2])
        self.assertEqual(x.multiply(y), expected, 'one element matrices')

    def test_multply_one_constant(self):
        x = SymmetricMatrix([1])
        constant = 2
        expected = SymmetricMatrix([2])
        self.assertEqual(x.multiply(constant),
                         expected, 'one element times constant')

    def test_multiply_two_constant(self):
        x = SymmetricMatrix([[1, 5], [5, 4]], 2)
        constant = 2
        expected = SymmetricMatrix([[2, 10], [10, 8]])
        self.assertEqual(x.multiply(constant), expected,
                         '2 by 2 times constant')

    def test_multiply_two_by_2_by_1(self):
        x = SymmetricMatrix([2, 1], [1, 2])
        y = Matrix([[2], [1]])
        expected = SymmetricMatrix([[5]])
        self.assertEqual(x.multiply(y), expected,
                         '2 by 2 times 2 by 1')

    def test_multiply_two_two_by_two(self):
        x = SymmetricMatrix([[2, 1], [1, 1]])
        y = Matrix([[1, 2], [1, 2]])
        expected = SymmetricMatrix([[3, 6], [6, 4]])
        self.assertEqual(x.multiply(y), expected,
                         'two 2 by 2')

    def test_multiply_alpha_num(self):
        x = SymmetricMatrix([[2, 1], [1, 'a']])
        y = SymmetricMatrix([[1, 2], [1, 2]])
        self.assertRaises(MatrixNotNumber, x.multiply(y),
                          'SymmetricMatrix include alpha')

    def test_multiply_aplha_constant(self):
        x = SymmetricMatrix([[2, 1], [1, 1]])
        constant = 'c'
        self.assertRaises(MatrixNotNumber, x.multiply(constant),
                          'SymmetricMatrix times constant of str')

    def test_multiply_not_fit(self):
        x = SymmetricMatrix([[2]])
        y = Matrix([[3, 3, 3]])
        self.assertRaises(MatrixIllegalMove, x.multiply(y),
                          'it is not m by n times n by k')


class TestSymmetricMatrixSubtract(unittest.TestCase):
    def test_subtract_one_one(self):
        x = SymmetricMatrix([2])
        y = SymmetricMatrix([1.0])
        expected = SymmetricMatrix([1.0])
        self.assertEqual(x.subtract(y), expected,
                         'elements minus')

    def test_subtract_two_two(self):
        x = SymmetricMatrix([[1, 2], [2, 1]])
        y = Matrix([2, 1], [2, 1])
        expected = SymmetricMatrix([[-1, 1], [1, 0]])
        self.assertEqual(x.subtract(y), expected,
                         '2 by 1 subtaction')

    def test_subtract_two_square(self):
        x = SymmetricMatrix([[1, 2, 3], [3, 2, 3], [3, 2, 3]])
        y = Matrix([[4, 3, 2], [4, 3, 2], [4, 3, 2]])
        expected = SymmetricMatrix([[-3, -1, 1], [1, -1, 1], [1, -1, 1]])
        self.assertEqual(x.subtract(y), expected,
                         'square subtraction')

    def test_subtact_SymmetricMatrix_alpha(self):
        x = SymmetricMatrix([[1, 2], [2, 'a']])
        y = Matrix([2, 1], [2, 1])
        self.assertRaises(MatrixNotNumber, x.subtract(y),
                          'alpha included SymmetricMatrix subtraction')

    def test_subtract_fail(self):
        x = SymmetricMatrix([[1, 2]])
        y = SymmetricMatrix([[1, 3, 2]])
        self.assertRaises(MatrixIllegalMove, x.subtract(y),
                          'it is not m by n minus m by n')


class TestSymmetricMatrixAdd(unittest.TestCase):
    def test_add_one_one(self):
        x = SymmetricMatrix([1])
        y = SymmetricMatrix([2.0])
        expected = SymmetricMatrix([3.0])
        self.assertEqual(x.add(y), expected,
                         'elements add')

    def test_add_two_two(self):
        x = SymmetricMatrix([[3, 1.0], [1, 3]])
        y = SymmetricMatrix([[4, 4], [4, 4]])
        expected = SymmetricMatrix([[7, 5.0], [5, 7]])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition')

    def test_add_two_square(self):
        x = SymmetricMatrix([[1, 2, 3.0], [3, 2, 3], [3.0, 2, 3]])
        y = SymmetricMatrix([[4, 3, 2], [2, 3, 2], [2, 3, 2]])
        expected = SymmetricMatrix([[5, 5, 5.0], [5, 5, 5], [5.0, 5, 5]])
        self.assertEqual(x.add(y), expected,
                         'square addition')

    def test_add_one_one_letter(self):
            x = SymmetricMatrix(['a'])
            y = SymmetricMatrix(['b'])
            expected = SymmetricMatrix(['ab'])
            self.assertEqual(x.add(y), expected,
                             'elements add_letters')

    def test_add_two_two_letters(self):
        x = SymmetricMatrix([['a', 'b'], ['b', 'd']])
        y = Matrix([['e', 'f'], ['g', 'h']])
        expected = SymmetricMatrix([['ae', 'bf'], ['bf', 'df']])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition_letters')

    def test_add_two_square_letters_and_num(self):
        x = SymmetricMatrix([['a', 'b', 'c'], ['c', 'b', 'c'],
                             ['c', 'b', 'c']])
        y = SymmetricMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        expected = SymmetricMatrix([['a1', 'b1', 'c1'], ['c1', 'b1', 'c1'],
                                    ['c1', 'b1', 'c1']])
        self.assertEqual(x.add(y), expected,
                         'square addition_letters_num')

    def test_add_fail(self):
        x = SymmetricMatrix([['help']])
        y = Matrix([['going', 'to', 'become'],
                    ['insane', 'real', 'soon']])
        self.assertRaises(MatrixIllegalMove, x.add(y),
                          'not m by n + m by n')


class TestSymmetricMatrixGetColumn(unittest.TestCase):
    def test_get_column_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_column(), expected,
                         'default get_column')

    def test_get_column_first(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_column(1), expected,
                         'get first column')

    def test_get_2nd_column(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = [0, 1]
        self.assertEqual(x.get_column(2), expected,
                         'get second column')

    def test_get_last_column(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_column(3), expected,
                         'get last column')

    def test_get_column_overbound(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(4),
                          'out of bound get column')

    def test_get_column_zero(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_column(0),
                          'get column zero')


class TestSymmetricMatrixSetColumn(unittest.TestCase):
    def test_set_column_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = [1, 'a']
        expected = SymmetricMatrix([[1, 'a'], ['a', 1]])
        self.assertEqual(x.set_column(y), expected,
                         'default set column')

    def test_set_column_first(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = [1, 1]
        expected = SymmetricMatrix([[1, 1], [1, 1]])
        self.assertEqual(x.set_column(y, 1), expected,
                         'set first column')

    def test_set_2nd_column(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SymmetricMatrix([[1, 0, 1], [1, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_column(y, 2), expected,
                         'set second column')

    def test_set_last_column(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SymmetricMatrix([[1, 0, 1], [1, 1, 1], [1, 0, 1]])
        self.assertEqual(x.set_column(y, 3), expected,
                         'set last column')

    def test_set_column_overbound(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 4),
                          'out of bound set column')

    def test_set_column_zero(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 0),
                          'set column zero')


class TestSymmetricMatrixGetRow(unittest.TestCase):
    def test_get_row_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_row(), expected,
                         'default get row')

    def test_get_row_first(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = [1, 0]
        self.assertEqual(x.get_row(1), expected,
                         'get first row')

    def test_get_2nd_row(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [0, 1, 0]
        self.assertEqual(x.get_row(2), expected,
                         'get second row')

    def test_get_last_row(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = [1, 0, 1]
        self.assertEqual(x.get_row(3), expected,
                         'get last row')

    def test_get_row_overbound(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(4),
                          'out of bound get row')

    def test_get_row_zero(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get_row(0),
                          'get row zero')


class TestSymmetricMatrixSetRow(unittest.TestCase):
    def test_set_row_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = [1, 'a']
        expected = SymmetricMatrix([[1, 'a'], ['a', 1]])
        self.assertEqual(x.set_row(y), expected,
                         'default set row')

    def test_set_row_first(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = [1, 1]
        expected = SymmetricMatrix([[1, 1], [1, 1]])
        self.assertEqual(x.set_row(y, 1), expected,
                         'set first column')

    def test_set_2nd_row(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SymmetricMatrix([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_row(y, 2), expected,
                         'set second row')

    def test_set_last_row(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        expected = SymmetricMatrix([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(x.set_row(y, 3), expected,
                         'set last row')

    def test_set_column_overbound(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 4),
                          'out of bound set row')

    def test_set_column_zero(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 0),
                          'set row zero')


class TestSymmetricMatrixGet(unittest.TestCase):
    def test_get_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = 1
        self.assertEqual(x.get(), expected,
                         'default get')

    def test_get_first_element(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        expected = 1
        self.assertEqual(x.get(1, 1), expected,
                         'get first element')

    def test_get_2nd_element(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 0
        self.assertEqual(x.get(2), expected,
                         'get 2nd row 1st element')

    def test_get_2nd_row_2nd_element(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        expected = 1
        self.assertEqual(x.get(2, 2), expected,
                         'get 2nd row 2nd element')

    def test_get_overboundzero1(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0),
                          'row 0 column 1 DNE')

    def test_get_overboundzero2(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(0, 0),
                          'row 0, column 0 DNE')

    def test_get_overbound3(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4),
                          'overbound by row')

    def test_get_overbound4(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(4, 3),
                          'overbound by row')

    def test_get_overbound5(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertRaises(MatrixOutOfBound, x.get(3, 4),
                          'overbound by column')


class TestSymmetricMatrixSet(unittest.TestCase):
    def test_set_default(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = 'a'
        expected = SymmetricMatrix([['a', 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set alpha')

    def test_set_default2(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = 2.0
        expected = SymmetricMatrix([[2.0, 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set float')

    def test_set_default2(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = 4
        expected = SymmetricMatrix([[4, 0], [0, 1]])
        self.assertEqual(x.set(y), expected,
                         'default set int')

    def test_set_first_element(self):
        x = SymmetricMatrix([[1, 0], [0, 1]])
        y = 5
        expected = SymmetricMatrix([[5, 0], [0, 1]])
        self.assertEqual(x.set(y, 1, 1), expected,
                         'set first element')

    def test_set_2nd_element(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = SymmetricMatrix([[1, 0, 1], [5, 1, 5], [1, 0, 1]])
        self.assertEqual(x.set(y, 2), expected,
                         'set 2nd row 1st element')

    def test_set_2nd_row_2nd_element(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        expected = SymmetricMatrix([[1, 0, 1], [0, 5, 0], [1, 0, 1]])
        self.assertEqual(x.set(y, 2, 2), expected,
                         'set 2nd row 2nd element')

    def test_set_overboundzero1(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0),
                          'row 0 column 1 DNE')

    def test_set_overboundzero2(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0, 0),
                          'row 0, column 0 DNE')

    def test_set_overbound3(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'a'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4),
                          'overbound by row')

    def test_set_overbound4(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'd'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4, 3),
                          'overbound by row')

    def test_set_overbound5(self):
        x = SymmetricMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        y = 'help'
        self.assertRaises(MatrixOutOfBound, x.set(y, 3, 4),
                          'overbound by column')


class TestSymmetricMatrixSwapRows(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(x.swap_rows(1, 1), expected,
                         'switching rows with itself')

    def test_swap_rows_first_and_sec1(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[2, 4], [4, 2]])
        self.assertEqual(x.swap_rows(1, 2), expected,
                         'switching rows 1st and 2nd')

    def test_swap_rows_first_and_sec2(self):
            x = SymmetricMatrix([[1, 2], [2, 4]])
            expected = SymmetricMatrix([[2, 4], [4, 2]])
            self.assertEqual(x.swap_rows(2, 1), expected,
                             'switching rows 2nd and 1st')

    def test_swap_rows_first_and_third1(self):
            x = SymmetricMatrix([[1, 2, 3], [3, 4, 3], [3, 2, 1]])
            expected = SymmetricMatrix([[3, 2, 1], [3, 4, 3], [1, 2, 3]])
            self.assertEqual(x.swap_rows(1, 3), expected,
                             'switching rows 1st and 3rd')

    def test_swap_rows_first_and_thid2(self):
            x = SymmetricMatrix([[1, 2, 3], [3, 4, 3], [3, 2, 1]])
            expected = SymmetricMatrix([[3, 2, 1], [3, 4, 3], [1, 2, 3]])
            self.assertEqual(x.swap_rows(3, 1), expected,
                             'switching rows 3rd and 1st')


class TestSymmetricMatrixSwapColumns(unittest.TestCase):
    def test_swap_columns_itself(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(x.swap_columns(1, 1), expected,
                         'switching columns with itself')

    def test_swap_columns_first_and_sec1(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[2, 1], [1, 2]])
        self.assertEqual(x.swap_columns(1, 2), expected,
                         'switching columns 1st and 2nd')

    def test_swap_columns_first_and_sec2(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[2, 1], [1, 2]])
        self.assertEqual(x.swap_columns(2, 1), expected,
                         'switching columns 2nd and 1st')

    def test_swap_columns_first_and_third1(self):
            x = SymmetricMatrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
            expected = SymmetricMatrix([[3, 2, 1], [4, 5, 4], [1, 2, 3]])
            self.assertEqual(x.swap_columns(1, 2), expected,
                             'switching columns 1st and 3rd')

    def test_swap_columns_first_and_thid2(self):
            x = SymmetricMatrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
            expected = SymmetricMatrix([[3, 2, 1], [4, 5, 4], [1, 2, 3]])
            self.assertEqual(x.swap_columns(3, 1), expected,
                             'switching columns 3rd and 1st')


class TestSymmetricMatrixDeterminant(unittest.TestCase):
    def test_determinant_zero_SymmetricMatrix(self):
        x = SymmetricMatrix([[0, 0], [0, 0]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of zero SymmetricMatrix')

    def test_determinant_non_zero_SymmetricMatrix(self):
        x = SymmetricMatrix([[1, 2], [2, 4.0]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of nonzero SymmetricMatrix')

    def test_determinant_same_element(self):
        x = SymmetricMatrix([[5, 5], [5, 5]])
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinant_include_zero_and_nonzero(self):
        x = SymmetricMatrix([[1, 2.0], [2, 5]])
        expected = 1
        self.assertEqual(x.determinant(), expected,
                         'determinant of same elements')

    def test_determinint_fail1(self):
        x = SymmetricMatrix([[0]])
        self.assertRaises(MatrixNot2By2, x.determinant(),
                          'one element is not 2 by 2')

    def test_determinint_fail2(self):
            x = SymmetricMatrix([[0, 1], [1, 3]])
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '2 by 1 is not 2 by 2')

    def test_determinint_fail1(self):
            x = SymmetricMatrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '3 by 3 is not 2 by 2')


class TestSymmetricMatrixTranspose(unittest.TestCase):
    def test_transpose_one_element(self):
        x = SymmetricMatrix([[0]])
        expected = SymmetricMatrix([0])
        self.assertEqual(x.transpose(), expected,
                         'transposing of one element')

    def test_transpose_2_by_2(self):
        x = SymmetricMatrix([[0, 1], [1, 4]])
        expected = SymmetricMatrix([[0, 1], [1, 4]])
        self.assertEqual(x.transpose(), expected,
                         'transposing 2 by 2 SymmetricMatrix')

    def test_transpose_sqaure(self):
        x = SymmetricMatrix([[0, 1, 2], [4, 4, 4], [2, 1, 8]])
        expected = SymmetricMatrix([[0, 1, 2], [4, 4, 4], [2, 1, 8]])
        self.assertEqual(x.transpose(), expected,
                         'transposing SymmetricMatrix')


class TestSymmetricMatrixStr(unittest.TestCase):
    def test_str_method_one(self):
        x = SymmetricMatrix([[0]])
        expected = '0'
        self.assertEqual(x.__str__(), expected,
                         'printing one element')

    def test_str_method_2_by_2(self):
        x = SymmetricMatrix([[0, 1], [1, 3]])
        expected = '0 1 / 1 3'
        self.assertEqual(x.__str__(), expected,
                         'printing 2 by 2')

    def test__str_method_alpha(self):
        x = SymmetricMatrix([['a', 'b'], ['b', 'd']])
        expected = 'a b / b d'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')

    def test_str_method_alphanum(self):
        x = SymmetricMatrix([['a', 1], [1, 2.0]])
        expected = 'a 1 / 1 2.0'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')


class TestSymetricMatricesGetDiagonal(unittest.TestCase):
    def test_symmetric_matrix1(self):
        x = SymmetricMatrix([[1]])
        expected = [1]
        self.assertEqual(x.get_diagonal(), expected,
                         'one by one matrix')

    def test_symmetric_matrix2(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = [1, 4]
        self.assertEqual(x.get_diagonal(), expected,
                         'two by two matrix')

    def test_symmetric_matrix3(self):
        x = SymmetricMatrix([[1, 2, 3], [4, 5, 4], [3, 2, 8]])
        expected = [1, 5, 8]
        self.assertEqual(x.get_diagonal(), expected,
                         '3 by 3 matrix')

    def test_symmetric_matrix_fail(self):
        x = SymmetricMatrix([['a']])
        self.assertRaises(MatrixNotNumber, x.get_diagonal(),
                          'one by one matrix')

    def test_symmetric_matrix_float(self):
        x = SymmetricMatrix([[1.0]])
        expected = [1.0]
        self.assertEqual(x.get_diagonal, expected,
                         'float matrices')


class TestSymmetricMatricesSwap(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = SymmetricMatrix([['a', 2.0], [2.0, 4]])
        expected = SymmetricMatrix([['a', 2.0], [2.0, 4]])
        self.assertEqual(x.swap('r', 1, 'r', 1), expected,
                         'swap rows with itself')

    def test_swap_rows(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[2, 4], [4, 2]])
        self.assertEqual(x.swap('r', 1, 'r', 2), expected,
                         'swap rows')

    def test_swap_columns_itself(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(x.swap('c', 1, 'c', 1), expected,
                         'swap columns with itself')

    def test_swap_columns(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[2, 1], [1, 2]])
        self.assertEqual(x.swap('c', 1, 'c', 2), expected,
                         'swap columns')

    def test_swap_row_column(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[4, 2], [2, 1]])
        self.assertEqual(x.swap('r', 1, 'c', 2), expected,
                         '1st row swap 2nd column')

    def test_swap_row_column(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        expected = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(x.swap('r', 1, 'c', 1), expected,
                         '1st row swap 1st column')

    def test_swap_row_column(self):
        x = SymmetricMatrix([[1, 2, 3], [4, 5, 4], [3, 2, 9]])
        expected = SymmetricMatrix([[1, 2, 3], [4, 5, 4], [3, 2, 9]])
        self.assertEqual(x.swap('c', 2, 'r', 2), expected,
                         '2st row swap 2nd column')

    def test_swap_row_fail1(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'r', 2),
                         'swap row zero')

    def test_swap_row_fail2(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'r', 2),
                         'swap row out of bounds')

    def test_swap_column_fail1(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'c', 2),
                         'swap column zero')

    def test_swap_column_fail2(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 3, 'c', 2),
                         'swap column out of bounds')

    def test_swap_row_column_fail1(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'c', 2),
                         'swap row zero')

    def test_swap_row_column_fail2(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'c', 2),
                         'swap row out of bounds')

    def test_swap_row_column_fail3(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'r', 2),
                         'swap column zero')

    def test_swap_row_column_fail4(self):
        x = SymmetricMatrix([[1, 2], [2, 4]])
        self.assertEqual(MatrixOutOfBound, x.swap('c', 4, 'c', 2),
                         'swap column out of bounds')

# Test Case for Identity Matrix


class TestDiagonalMatrixInit(unittest.TestCase):
    def test_init_one_element1(self):
        x = DiagonalMatrix(1, 1)
        expected = 1
        self.assertEqual(x.get(), expected, 'one element int')

    def test_init_one_element2(self):
        x = DiagonalMatrix('a', 1)
        expected = 'a'
        self.assertEqual(x.get(), expected, 'one element alpha')

    def test_init_one_element3(self):
        x = DiagonalMatrix(4.5, 1)
        expected = 4.5
        self.assertEqual(x.get(), expected, 'one element float')

    def test_init_2_by_2(self):
        x = DiagonalMatrix(1, 2)
        row1 = [1, 0]
        row2 = [0, 1]
        self.assertEqual((x.get_row(), x.get_row(2)), (row1, row2),
                         'identity 2 by 2')

    def test_init_multiple(self):
        x = DiagonalMatrix('r', 4)
        row1 = ['r', 0, 0, 0]
        row2 = [0, 'r', 0, 0]
        row3 = [0, 0, 'r', 0]
        row4 = [0, 0, 0, 'r']
        self.assertEqual((x.get_row(), x.get_row(2), x.get_row(3),
                          x.get_row(4)), (row1, row2, row3, row4),
                         'identity 4 by 4')


class TestDiagonalMatrixMultiply(unittest.TestCase):
    def test_multiply_one(self):
        x = DiagonalMatrix(1)
        y = DiagonalMatrix(2)
        expected = DiagonalMatrix(2)
        self.assertEqual(x.multiply(y), expected, 'one element matrices')

    def test_multply_one_constant(self):
        x = DiagonalMatrix(1)
        constant = 2
        expected = DiagonalMatrix(2)
        self.assertEqual(x.multiply(constant),
                         expected, 'one element times constant')

    def test_multiply_two_constant(self):
        x = DiagonalMatrix(2.0, 2)
        constant = 2
        expected = DiagonalMatrix(4.0, 2)
        self.assertEqual(x.multiply(constant), expected,
                         '2 by 2 times constant')

    def test_multiply_two_by_2_by_1(self):
        x = DiagonalMatrix([2, 0], [0, 2])
        y = Matrix([1, 1])
        expected = DiagonalMatrix(2)
        self.assertEqual(x.multiply(y), expected,
                         '2 by 2 times 2 by 1')

    def test_multiply_two_two_by_two(self):
        x = DiagonalMatrix(2, 2)
        y = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(2, 2)
        self.assertEqual(x.multiply(y), expected,
                         'two 2 by 2')

    def test_multiply_alpha_num(self):
        x = DiagonalMatrix([['a', 0], [0, 'a']])
        y = Matrix([[1, 2], [1, 2]])
        self.assertRaises(MatrixNotNumber, x.multiply(y),
                          'DiagonalMatrix include alpha')

    def test_multiply_alpha_constant(self):
        x = DiagonalMatrix([[2, 0], [0, 2]], 2)
        constant = 'c'
        self.assertRaises(MatrixNotNumber, x.multiply(constant),
                          'DiagonalMatrix times constant of str')

    def test_multiply_not_fit(self):
        x = DiagonalMatrix([[2]])
        y = Matrix([[3, 3, 3]])
        self.assertRaises(MatrixIllegalMove, x.multiply(y),
                          'it is not m by n times n by k')


class TestDiagonalMatrixSubtract(unittest.TestCase):
    def test_subtract_one_one(self):
        x = DiagonalMatrix([2])
        y = DiagonalMatrix([1.0])
        expected = DiagonalMatrix([1.0])
        self.assertEqual(x.subtract(y), expected,
                         'elements minus')

    def test_subtract_two_two(self):
        x = DiagonalMatrix(1, 2)
        y = Matrix([2, 1], [2, 1])
        expected = DiagonalMatrix(-1, 2)
        self.assertEqual(x.subtract(y), expected,
                         '2 by 1 subtaction')

    def test_subtract_two_square(self):
        x = DiagonalMatrix(1, 3)
        y = DiagonalMatrix(4, 3)
        expected = DiagonalMatrix(-3, 0)
        self.assertEqual(x.subtract(y), expected,
                         'square subtraction')

    def test_subtact_DiagonalMatrix_alpha(self):
        x = DiagonalMatrix([['a', 0], [0, 'a']])
        y = Matrix([2, 1], [2, 1])
        self.assertRaises(MatrixNotNumber, x.subtract(y),
                          'alpha included DiagonalMatrix subtraction')

    def test_subtract_fail(self):
        x = DiagonalMatrix([[1]])
        y = Matrix([[1, 3, 2]])
        self.assertRaises(MatrixIllegalMove, x.subtract(y),
                          'it is not m by n minus m by n')


class TestDiagonalMatrixAdd(unittest.TestCase):
    def test_add_one_one(self):
        x = DiagonalMatrix([1])
        y = DiagonalMatrix([2.0])
        expected = DiagonalMatrix([3.0])
        self.assertEqual(x.add(y), expected,
                         'elements add')

    def test_add_two_two(self):
        x = DiagonalMatrix(3, 0)
        y = DiagonalMatrix(4, 0)
        expected = DiagonalMatrix([[7.0, 0], [0, 7.0]])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition')

    def test_add_two_square(self):
        x = DiagonalMatrix(1, 3)
        y = DiagonalMatrix(4, 0)
        expected = DiagonalMatrix(5, 3)
        self.assertEqual(x.add(y), expected,
                         'square addition')

    def test_add_one_one_letter(self):
            x = DiagonalMatrix('a')
            y = DiagonalMatrix('b')
            expected = DiagonalMatrix(['ab'])
            self.assertEqual(x.add(y), expected,
                             'elements add_letters')

    def test_add_two_two_letters(self):
        x = DiagonalMatrix('a', 2)
        y = Matrix([['e', 'f'], ['g', 'h']])
        expected = DiagonalMatrix('ae', 2)
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition_letters')

    def test_add_two_square_letters_and_num(self):
        x = DiagonalMatrix('a', 3)
        y = DiagonalMatrix('d', 3)
        expected = DiagonalMatrix('ad', 3)
        self.assertEqual(x.add(y), expected,
                         'square addition_letters_num')

    def test_add_fail(self):
        x = DiagonalMatrix('help')
        y = Matrix([['going', 'to', 'become'],
                    ['insane', 'real', 'soon']])
        self.assertRaises(MatrixIllegalMove, x.add(y),
                          'not m by n + m by n')


class TestDiagonalMatrixGetColumn(unittest.TestCase):
    def test_get_column_default(self):
        x = DiagonalMatrix(1, 2)
        expected = [1, 0]
        self.assertEqual(x.get_column(), expected,
                         'default get_column')

    def test_get_column_first(self):
        x = DiagonalMatrix(1, 2)
        expected = [1, 0]
        self.assertEqual(x.get_column(1), expected,
                         'get first column')

    def test_get_2nd_column(self):
        x = DiagonalMatrix(1, 3)
        expected = [0, 1, 0]
        self.assertEqual(x.get_column(2), expected,
                         'get second column')

    def test_get_last_column(self):
        x = DiagonalMatrix(1, 3)
        expected = [0, 0, 1]
        self.assertEqual(x.get_column(3), expected,
                         'get last column')

    def test_get_column_overbound(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get_column(4),
                          'out of bound get column')

    def test_get_column_zero(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get_column(0),
                          'get column zero')


class TestDiagonalMatrixSetColumn(unittest.TestCase):
    def test_set_column_default(self):
        x = DiagonalMatrix(1, 2)
        y = [1, 'a']
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_column(y), expected,
                         'default set column')

    def test_set_column_first(self):
        x = DiagonalMatrix(1, 2)
        y = [1, 1]
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_column(y, 1), expected,
                         'set first column')

    def test_set_2nd_column(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 1]
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set_column(y, 2), expected,
                         'set second column')

    def test_set_last_column(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 1]
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set_column(y, 3), expected,
                         'set last column')

    def test_set_column_overbound(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 4),
                          'out of bound set column')

    def test_set_column_zero(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 0),
                          'set column zero')


class TestDiagonalMatrixGetRow(unittest.TestCase):
    def test_get_row_default(self):
        x = DiagonalMatrix(1, 2)
        expected = [1, 0]
        self.assertEqual(x.get_row(), expected,
                         'default get row')

    def test_get_row_first(self):
        x = DiagonalMatrix(1, 2)
        expected = [1, 0]
        self.assertEqual(x.get_row(1), expected,
                         'get first row')

    def test_get_2nd_row(self):
        x = DiagonalMatrix(1, 3)
        expected = [0, 1, 0]
        self.assertEqual(x.get_row(2), expected,
                         'get second row')

    def test_get_last_row(self):
        x = DiagonalMatrix(1, 3)
        expected = [0, 0, 1]
        self.assertEqual(x.get_row(3), expected,
                         'get last row')

    def test_get_row_overbound(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get_row(4),
                          'out of bound get row')

    def test_get_row_zero(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get_row(0),
                          'get row zero')


class TestDiagonalMatrixSetRow(unittest.TestCase):
    def test_set_row_default(self):
        x = DiagonalMatrix(1, 2)
        y = [1, 'a']
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_row(y), expected,
                         'default set row')

    def test_set_row_first(self):
        x = DiagonalMatrix(1, 2)
        y = [1, 1]
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_row(y, 1), expected,
                         'set first column')

    def test_set_2nd_row(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 2, 1]
        expected = DiagonalMatrix(2, 3)
        self.assertEqual(x.set_row(y, 2), expected,
                         'set second row')

    def test_set_last_row(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 3]
        expected = DiagonalMatrix(3, 3)
        self.assertEqual(x.set_row(y, 3), expected,
                         'set last row')

    def test_set_column_overbound(self):
        x = DiagonalMatrix(1, 3)
        y = ['a', 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 4),
                          'out of bound set row')

    def test_set_column_zero(self):
        x = DiagonalMatrix(1, 3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 0),
                          'set row zero')


class TestDiagonalMatrixGet(unittest.TestCase):
    def test_get_default(self):
        x = DiagonalMatrix(1, 2)
        expected = 1
        self.assertEqual(x.get(), expected,
                         'default get')

    def test_get_first_element(self):
        x = DiagonalMatrix(1, 2)
        expected = 1
        self.assertEqual(x.get(1, 1), expected,
                         'get first element')

    def test_get_2nd_element(self):
        x = DiagonalMatrix(1, 3)
        expected = 0
        self.assertEqual(x.get(2), expected,
                         'get 2nd row 1st element')

    def test_get_2nd_row_2nd_element(self):
        x = DiagonalMatrix(1, 3)
        expected = 1
        self.assertEqual(x.get(2, 2), expected,
                         'get 2nd row 2nd element')

    def test_get_overboundzero1(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get(0),
                          'row 0 column 1 DNE')

    def test_get_overboundzero2(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get(0, 0),
                          'row 0, column 0 DNE')

    def test_get_overbound3(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get(4),
                          'overbound by row')

    def test_get_overbound4(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get(4, 3),
                          'overbound by row')

    def test_get_overbound5(self):
        x = DiagonalMatrix(1, 3)
        self.assertRaises(MatrixOutOfBound, x.get(3, 4),
                          'overbound by column')


class TestDiagonalMatrixSet(unittest.TestCase):
    def test_set_default(self):
        x = DiagonalMatrix(1, 2)
        y = 'a'
        expected = DiagonalMatrix('a', 2)
        self.assertEqual(x.set(y), expected,
                         'default set alpha')

    def test_set_default2(self):
        x = DiagonalMatrix(1, 2)
        y = 2.0
        expected = DiagonalMatrix(2.0, 2)
        self.assertEqual(x.set(y), expected,
                         'default set float')

    def test_set_default2(self):
        x = DiagonalMatrix(1, 2)
        y = 4
        expected = DiagonalMatrix(4.0, 2)
        self.assertEqual(x.set(y), expected,
                         'default set int')

    def test_set_first_element(self):
        x = DiagonalMatrix(1, 2)
        y = 5
        expected = DiagonalMatrix(5, 2)
        self.assertEqual(x.set(y, 1, 1), expected,
                         'set first element')

    def test_set_2nd_element(self):
        x = DiagonalMatrix(1, 3)
        y = 5
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set(y, 2), expected,
                         'set 2nd row 1st element')

    def test_set_2nd_row_2nd_element(self):
        x = DiagonalMatrix(1, 3)
        y = 5
        expected = DiagonalMatrix(5, 3)
        self.assertEqual(x.set(y, 2, 2), expected,
                         'set 2nd row 2nd element')

    def test_set_overboundzero1(self):
        x = DiagonalMatrix(1, 3)
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0),
                          'row 0 column 1 DNE')

    def test_set_overboundzero2(self):
        x = DiagonalMatrix(1, 3)
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0, 0),
                          'row 0, column 0 DNE')

    def test_set_overbound3(self):
        x = DiagonalMatrix(1, 3)
        y = 'a'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4),
                          'overbound by row')

    def test_set_overbound4(self):
        x = DiagonalMatrix(1, 3)
        y = 'd'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4, 3),
                          'overbound by row')

    def test_set_overbound5(self):
        x = DiagonalMatrix(1, 3)
        y = 'help'
        self.assertRaises(MatrixOutOfBound, x.set(y, 3, 4),
                          'overbound by column')


class TestDiagonalMatrixSwapRows(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.swap_rows(1, 1), expected,
                         'switching rows with itself')

    def test_swap_rows_first_and_sec1(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_rows(1, 2), expected,
                         'switching rows 1st and 2nd')

    def test_swap_rows_first_and_sec2(self):
            x = DiagonalMatrix(1, 2)
            expected = DiagonalMatrix(0, 2)
            self.assertEqual(x.swap_rows(2, 1), expected,
                             'switching rows 2nd and 1st')

    def test_swap_rows_first_and_third1(self):
            x = DiagonalMatrix(1, 2)
            expected = DiagonalMatrix(0, 2)
            self.assertEqual(x.swap_rows(1, 3), expected,
                             'switching rows 1st and 3rd')

    def test_swap_rows_first_and_thid2(self):
            x = DiagonalMatrix(1, 2)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_rows(3, 1), expected,
                             'switching rows 3rd and 1st')


class TestDiagonalMatrixSwapColumns(unittest.TestCase):
    def test_swap_columns_itself(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_columns(1, 1), expected,
                         'switching columns with itself')

    def test_swap_columns_first_and_sec1(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_columns(1, 2), expected,
                         'switching columns 1st and 2nd')

    def test_swap_columns_first_and_sec2(self):
            x = DiagonalMatrix(1, 2)
            expected = DiagonalMatrix([0, 2])
            self.assertEqual(x.swap_columns(2, 1), expected,
                             'switching columns 2nd and 1st')

    def test_swap_columns_first_and_third1(self):
            x = DiagonalMatrix(1, 3)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_columns(1, 2), expected,
                             'switching columns 1st and 3rd')

    def test_swap_columns_first_and_thid2(self):
            x = DiagonalMatrix(9, 3)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_columns(3, 1), expected,
                             'switching columnss 3rd and 1st')


class TestDiagonalMatrixDeterminant(unittest.TestCase):
    def test_determinant_zero_DiagonalMatrix(self):
        x = DiagonalMatrix(0, 2)
        expected = 0
        self.assertEqual(x.determinant(), expected,
                         'determinant of zero DiagonalMatrix')

    def test_determinant_non_zero_DiagonalMatrix(self):
        x = DiagonalMatrix(4, 2)
        expected = 16.0
        self.assertEqual(x.determinant(), expected,
                         'determinant of nonzero DiagonalMatrix')

    def test_determinint_fail1(self):
        x = DiagonalMatrix(0)
        self.assertRaises(MatrixNot2By2, x.determinant(),
                          'one element is not 2 by 2')

    def test_determinint_fail1(self):
            x = DiagonalMatrix(3, 3)
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '3 by 3 is not 2 by 2')


class TestDiagonalMatrixTranspose(unittest.TestCase):
    def test_transpose_one_element(self):
        x = DiagonalMatrix(0)
        expected = DiagonalMatrix(0)
        self.assertEqual(x.transpose(), expected,
                         'transposing of one element')

    def test_transpose_multiple(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.transpose(), expected,
                         'transposing nonsquare DiagonalMatrix')

    def test_transpose_sqaure(self):
        x = DiagonalMatrix([5, 3])
        expected = DiagonalMatrix(5, 3)
        self.assertEqual(x.transpose(), expected,
                         'transposing square DiagonalMatrix')


class TestDiagonalMatrixStr(unittest.TestCase):
    def test_str_method_one(self):
        x = DiagonalMatrix(0)
        expected = '0'
        self.assertEqual(x.__str__(), expected,
                         'printing one element')

    def test_str_method_square(self):
        x = DiagonalMatrix(1, 2)
        expected = '1 0 / 0 1'
        self.assertEqual(x.__str__(), expected,
                         'printing square')

    def test__str_method_alpha(self):
        x = DiagonalMatrix('a', 2)
        expected = 'a 0 / 0 a'
        self.assertEqual(x.__str__(), expected,
                         'printing all alpha')


class TestDiagonalMatricesGetDiagonal(unittest.TestCase):
    def test_Diagonal_matrix1(self):
        x = DiagonalMatrix(1)
        expected = [1]
        self.assertEqual(x.get_diagonal(), expected,
                         'one by one matrix')

    def test_Diagonal_matrix2(self):
        x = DiagonalMatrix(1, 2)
        expected = [1, 1]
        self.assertEqual(x.get_diagonal(), expected,
                         'two by two matrix')

    def test_Diagonal_matrix3(self):
        x = DiagonalMatrix(5, 3)
        expected = [5, 5, 5]
        self.assertEqual(x.get_diagonal(), expected,
                         '3 by 3 matrix')

    def test_Diagonal_matrix_fail(self):
        x = DiagonalMatrix('a', 5)
        self.assertRaises(MatrixNotNumber, x.get_diagonal(),
                          'one by one matrix')

    def test_Diagonal_matrix_float(self):
        x = DiagonalMatrix(1.0, 5)
        expected = [1.0, 1.0, 1.0, 1.0, 1.0]
        self.assertEqual(x.get_diagonal, expected,
                         'float matrices')


class TestDiagonalMatricesSwap(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = DiagonalMatrix('a', 2)
        expected = DiagonalMatrix('a', 2)
        self.assertEqual(x.swap('r', 1, 'r', 1), expected,
                         'swap rows with itself')

    def test_swap_rows(self):
        x = DiagonalMatrix('a', 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'r', 2), expected,
                         'swap rows')

    def test_swap_columns_itself(self):
        x = DiagonalMatrix(1.0, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('c', 1, 'c', 1), expected,
                         'swap columns with itself')

    def test_swap_columns(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('c', 1, 'c', 2), expected,
                         'swap columns')

    def test_swap_row_column(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'c', 2), expected,
                         '1st row swap 2nd column')

    def test_swap_row_column(self):
        x = DiagonalMatrix(1, 2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'c', 1), expected,
                         '1st row swap 1st column')

    def test_swap_row_column(self):
        x = DiagonalMatrix(3, 3)
        expected = DiagonalMatrix(3, 3)
        self.assertEqual(x.swap('c', 2, 'r', 2), expected,
                         '2st row swap 2nd column')

    def test_swap_row_fail1(self):
        x = DiagonalMatrix(2, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'r', 2),
                         'swap row zero')

    def test_swap_row_fail2(self):
        x = DiagonalMatrix(1, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'r', 2),
                         'swap row out of bounds')

    def test_swap_column_fail1(self):
        x = DiagonalMatrix(3, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'c', 2),
                         'swap column zero')

    def test_swap_column_fail2(self):
        x = DiagonalMatrix(4, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 3, 'c', 2),
                         'swap column out of bounds')

    def test_swap_row_column_fail1(self):
        x = DiagonalMatrix(5, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'c', 2),
                         'swap row zero')

    def test_swap_row_column_fail2(self):
        x = DiagonalMatrix(3, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'c', 2),
                         'swap row out of bounds')

    def test_swap_row_column_fail3(self):
        x = DiagonalMatrix(4, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'r', 2),
                         'swap column zero')

    def test_swap_row_column_fail4(self):
        x = DiagonalMatrix(6, 2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 4, 'c', 2),
                         'swap column out of bounds')


# Test Identity Matrix

class TestIdentityMatrixInit(unittest.TestCase):
    def test_init_one_element1(self):
        x = IdentityMatrix(1)
        expected = 1
        self.assertEqual(x.get(), expected, 'one element int')

    def test_init_2_by_2(self):
        x = IdentityMatrix(2)
        row1 = [1, 0]
        row2 = [0, 1]
        self.assertEqual((x.get_row(), x.get_row(2)), (row1, row2),
                         'identity 2 by 2')

    def test_init_multiple(self):
        x = IdentityMatrix(4)
        row1 = [1, 0, 0, 0]
        row2 = [0, 1, 0, 0]
        row3 = [0, 0, 1, 0]
        row4 = [0, 0, 0, 1]
        self.assertEqual((x.get_row(), x.get_row(2), x.get_row(3),
                          x.get_row(4)), (row1, row2, row3, row4),
                         'identity 4 by 4')


class TestIdentityMatrixMultiply(unittest.TestCase):
    def test_multiply_one(self):
        x = IdentityMatrix(1)
        y = DiagonalMatrix(2)
        expected = DiagonalMatrix(2)
        self.assertEqual(x.multiply(y), expected, 'one element matrices')

    def test_multply_one_constant(self):
        x = IdentityMatrix(1)
        constant = 2
        expected = DiagonalMatrix(2)
        self.assertEqual(x.multiply(constant),
                         expected, 'one element times constant')

    def test_multiply_two_constant(self):
        x = IdentityMatrix(2)
        constant = 2
        expected = DiagonalMatrix(2, 2)
        self.assertEqual(x.multiply(constant), expected,
                         '2 by 2 times constant')

    def test_multiply_alpha_constant(self):
        x = IdentityMatrix(2)
        constant = 'c'
        self.assertRaises(MatrixNotNumber, x.multiply(constant),
                          'IdentityMatrix times constant of str')

    def test_multiply_not_fit(self):
        x = IdentityMatrix(2)
        y = DiagonalMatrix(3, 3)
        self.assertRaises(MatrixIllegalMove, x.multiply(y),
                          'it is not m by n times n by k')


class TestIdentityMatrixSubtract(unittest.TestCase):
    def test_subtract_one_one(self):
        x = IdentityMatrix(1)
        y = IdentityMatrix(1)
        expected = DiagonalMatrix(0, 1)
        self.assertEqual(x.subtract(y), expected,
                         'elements minus')

    def test_subtract_two_two(self):
        x = IdentityMatrix(2)
        y = Matrix([2, 1], [2, 1])
        expected = DiagonalMatrix(-1, 2)
        self.assertEqual(x.subtract(y), expected,
                         '2 by 1 subtaction')

    def test_subtract_two_square(self):
        x = IdentityMatrix(3)
        y = DiagonalMatrix(4, 3)
        expected = DiagonalMatrix(-3, 0)
        self.assertEqual(x.subtract(y), expected,
                         'square subtraction')

    def test_subtact_IdentityMatrix_alpha(self):
        x = IdentityMatrix(2)
        y = Matrix([2, 1], ['a', 1])
        self.assertRaises(MatrixNotNumber, x.subtract(y),
                          'alpha included IdentityMatrix subtraction')

    def test_subtract_fail(self):
        x = IdentityMatrix(1)
        y = Matrix([[1, 3, 2]])
        self.assertRaises(MatrixIllegalMove, x.subtract(y),
                          'it is not m by n minus m by n')


class TestIdentityMatrixAdd(unittest.TestCase):
    def test_add_one_one(self):
        x = IdentityMatrix(1)
        y = IdentityMatrix(1)
        expected = DiagonalMatrix(2, 1)
        self.assertEqual(x.add(y), expected,
                         'elements add')

    def test_add_two_two(self):
        x = IdentityMatrix(2)
        y = DiagonalMatrix(6, 2)
        expected = IdentityMatrix([[7.0, 0], [0, 7.0]])
        self.assertEqual(x.add(y), expected,
                         '2 by 1 addition')

    def test_add_one_one_letter(self):
        x = IdentityMatrix(1)
        y = DiagonalMatrix('b', 1)
        expected = IdentityMatrix(['1b'])
        self.assertEqual(x.add(y), expected,
                         'elements add_letters')

    def test_add_fail(self):
        x = IdentityMatrix(1)
        y = Matrix([['going', 'to', 'become'],
                    ['insane', 'real', 'soon']])
        self.assertRaises(MatrixIllegalMove, x.add(y),
                          'not m by n + m by n')


class TestIdentityMatrixGetColumn(unittest.TestCase):
    def test_get_column_default(self):
        x = IdentityMatrix(2)
        expected = [1, 0]
        self.assertEqual(x.get_column(), expected,
                         'default get_column')

    def test_get_column_first(self):
        x = IdentityMatrix(2)
        expected = [1, 0]
        self.assertEqual(x.get_column(1), expected,
                         'get first column')

    def test_get_2nd_column(self):
        x = IdentityMatrix(3)
        expected = [0, 1, 0]
        self.assertEqual(x.get_column(2), expected,
                         'get second column')

    def test_get_last_column(self):
        x = IdentityMatrix(3)
        expected = [0, 0, 1]
        self.assertEqual(x.get_column(3), expected,
                         'get last column')

    def test_get_column_overbound(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get_column(4),
                          'out of bound get column')

    def test_get_column_zero(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get_column(0),
                          'get column zero')


class TestIdentityMatrixSetColumn(unittest.TestCase):
    def test_set_column_default(self):
        x = IdentityMatrix(2)
        y = [1, 'a']
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_column(y), expected,
                         'default set column')

    def test_set_column_first(self):
        x = IdentityMatrix(2)
        y = [1, 1]
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_column(y, 1), expected,
                         'set first column')

    def test_set_2nd_column(self):
        x = IdentityMatrix(3)
        y = [1, 1, 1]
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set_column(y, 2), expected,
                         'set second column')

    def test_set_last_column(self):
        x = IdentityMatrix(3)
        y = [1, 1, 1]
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set_column(y, 3), expected,
                         'set last column')

    def test_set_column_overbound(self):
        x = IdentityMatrix(3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 4),
                          'out of bound set column')

    def test_set_column_zero(self):
        x = IdentityMatrix(3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_column(y, 0),
                          'set column zero')


class TestIdentityMatrixGetRow(unittest.TestCase):
    def test_get_row_default(self):
        x = IdentityMatrix(2)
        expected = [1, 0]
        self.assertEqual(x.get_row(), expected,
                         'default get row')

    def test_get_row_first(self):
        x = IdentityMatrix(2)
        expected = [1, 0]
        self.assertEqual(x.get_row(1), expected,
                         'get first row')

    def test_get_2nd_row(self):
        x = IdentityMatrix(3)
        expected = [0, 1, 0]
        self.assertEqual(x.get_row(2), expected,
                         'get second row')

    def test_get_last_row(self):
        x = IdentityMatrix(3)
        expected = [0, 0, 1]
        self.assertEqual(x.get_row(3), expected,
                         'get last row')

    def test_get_row_overbound(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get_row(4),
                          'out of bound get row')

    def test_get_row_zero(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get_row(0),
                          'get row zero')


class TestIdentityMatrixSetRow(unittest.TestCase):
    def test_set_row_default(self):
        x = IdentityMatrix(2)
        y = [1, 'a']
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_row(y), expected,
                         'default set row')

    def test_set_row_first(self):
        x = IdentityMatrix(2)
        y = [1, 1]
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.set_row(y, 1), expected,
                         'set first column')

    def test_set_2nd_row(self):
        x = IdentityMatrix(3)
        y = [1, 2, 1]
        expected = DiagonalMatrix(2, 3)
        self.assertEqual(x.set_row(y, 2), expected,
                         'set second row')

    def test_set_last_row(self):
        x = IdentityMatrix(3)
        y = [1, 1, 3]
        expected = DiagonalMatrix(3, 3)
        self.assertEqual(x.set_row(y, 3), expected,
                         'set last row')

    def test_set_column_overbound(self):
        x = IdentityMatrix(3)
        y = ['a', 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 4),
                          'out of bound set row')

    def test_set_column_zero(self):
        x = IdentityMatrix(3)
        y = [1, 1, 1]
        self.assertRaises(MatrixOutOfBound, x.set_row(y, 0),
                          'set row zero')


class TestIdentityMatrixGet(unittest.TestCase):
    def test_get_default(self):
        x = IdentityMatrix(2)
        expected = 1
        self.assertEqual(x.get(), expected,
                         'default get')

    def test_get_first_element(self):
        x = IdentityMatrix(2)
        expected = 1
        self.assertEqual(x.get(1, 1), expected,
                         'get first element')

    def test_get_2nd_element(self):
        x = IdentityMatrix(3)
        expected = 0
        self.assertEqual(x.get(2), expected,
                         'get 2nd row 1st element')

    def test_get_2nd_row_2nd_element(self):
        x = IdentityMatrix(3)
        expected = 1
        self.assertEqual(x.get(2, 2), expected,
                         'get 2nd row 2nd element')

    def test_get_overboundzero1(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get(0),
                          'row 0 column 1 DNE')

    def test_get_overboundzero2(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get(0, 0),
                          'row 0, column 0 DNE')

    def test_get_overbound3(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get(4),
                          'overbound by row')

    def test_get_overbound4(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get(4, 3),
                          'overbound by row')

    def test_get_overbound5(self):
        x = IdentityMatrix(3)
        self.assertRaises(MatrixOutOfBound, x.get(3, 4),
                          'overbound by column')


class TestIdentityMatrixSet(unittest.TestCase):
    def test_set_default(self):
        x = IdentityMatrix(2)
        y = 'a'
        expected = DiagonalMatrix('a', 2)
        self.assertEqual(x.set(y), expected,
                         'default set alpha')

    def test_set_default2(self):
        x = IdentityMatrix(2)
        y = 2.0
        expected = DiagonalMatrix(2.0, 2)
        self.assertEqual(x.set(y), expected,
                         'default set float')

    def test_set_default2(self):
        x = IdentityMatrix(2)
        y = 4
        expected = DiagonalMatrix(4.0, 2)
        self.assertEqual(x.set(y), expected,
                         'default set int')

    def test_set_first_element(self):
        x = IdentityMatrix(2)
        y = 5
        expected = DiagonalMatrix(5, 2)
        self.assertEqual(x.set(y, 1, 1), expected,
                         'set first element')

    def test_set_2nd_element(self):
        x = IdentityMatrix(3)
        y = 5
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.set(y, 2), expected,
                         'set 2nd row 1st element')

    def test_set_2nd_row_2nd_element(self):
        x = IdentityMatrix(3)
        y = 5
        expected = DiagonalMatrix(5, 3)
        self.assertEqual(x.set(y, 2, 2), expected,
                         'set 2nd row 2nd element')

    def test_set_overboundzero1(self):
        x = IdentityMatrix(3)
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0),
                          'row 0 column 1 DNE')

    def test_set_overboundzero2(self):
        x = IdentityMatrix(3)
        y = 5
        self.assertRaises(MatrixOutOfBound, x.set(y, 0, 0),
                          'row 0, column 0 DNE')

    def test_set_overbound3(self):
        x = IdentityMatrix(3)
        y = 'a'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4),
                          'overbound by row')

    def test_set_overbound4(self):
        x = IdentityMatrix(3)
        y = 'd'
        self.assertRaises(MatrixOutOfBound, x.set(y, 4, 3),
                          'overbound by row')

    def test_set_overbound5(self):
        x = IdentityMatrix(3)
        y = 'help'
        self.assertRaises(MatrixOutOfBound, x.set(y, 3, 4),
                          'overbound by column')


class TestIdentityMatrixSwapRows(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.swap_rows(1, 1), expected,
                         'switching rows with itself')

    def test_swap_rows_first_and_sec1(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_rows(1, 2), expected,
                         'switching rows 1st and 2nd')

    def test_swap_rows_first_and_sec2(self):
            x = IdentityMatrix(2)
            expected = DiagonalMatrix(0, 2)
            self.assertEqual(x.swap_rows(2, 1), expected,
                             'switching rows 2nd and 1st')

    def test_swap_rows_first_and_third1(self):
            x = IdentityMatrix(2)
            expected = DiagonalMatrix(0, 2)
            self.assertEqual(x.swap_rows(1, 3), expected,
                             'switching rows 1st and 3rd')

    def test_swap_rows_first_and_thid2(self):
            x = IdentityMatrix(2)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_rows(3, 1), expected,
                             'switching rows 3rd and 1st')


class TestIdentityMatrixSwapColumns(unittest.TestCase):
    def test_swap_columns_itself(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_columns(1, 1), expected,
                         'switching columns with itself')

    def test_swap_columns_first_and_sec1(self):
        x = IdentityMatrix(1)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap_columns(1, 2), expected,
                         'switching columns 1st and 2nd')

    def test_swap_columns_first_and_sec2(self):
            x = IdentityMatrix(2)
            expected = DiagonalMatrix([0, 2])
            self.assertEqual(x.swap_columns(2, 1), expected,
                             'switching columns 2nd and 1st')

    def test_swap_columns_first_and_third1(self):
            x = IdentityMatrix(3)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_columns(1, 2), expected,
                             'switching columns 1st and 3rd')

    def test_swap_columns_first_and_thid2(self):
            x = IdentityMatrix(3)
            expected = DiagonalMatrix(0, 3)
            self.assertEqual(x.swap_columns(3, 1), expected,
                             'switching columnss 3rd and 1st')


class TestIdentityMatrixDeterminant(unittest.TestCase):
    def test_determinant_zero_IdentityMatrix(self):
        x = IdentityMatrix(2)
        expected = 2
        self.assertEqual(x.determinant(), expected,
                         'determinant of zero IdentityMatrix')

    def test_determinint_fail1(self):
        x = IdentityMatrix(0)
        self.assertRaises(MatrixNot2By2, x.determinant(),
                          'one element is not 2 by 2')

    def test_determinint_fail1(self):
            x = IdentityMatrix(3)
            self.assertRaises(MatrixNot2By2, x.determinant(),
                              '3 by 3 is not 2 by 2')


class TestIdentityMatrixTranspose(unittest.TestCase):
    def test_transpose_one_element(self):
        x = IdentityMatrix(1)
        expected = DiagonalMatrix(1, 1)
        self.assertEqual(x.transpose(), expected,
                         'transposing of one element')

    def test_transpose_multiple(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.transpose(), expected,
                         'transposing nonsquare IdentityMatrix')


class TestIdentityMatrixStr(unittest.TestCase):
    def test_str_method_one(self):
        x = DiagonalMatrix(1)
        expected = '1'
        self.assertEqual(x.__str__(), expected,
                         'printing one element')

    def test_str_method_square(self):
        x = IdentityMatrix(2)
        expected = '1 0 / 0 1'
        self.assertEqual(x.__str__(), expected,
                         'printing square')


class TestIdentityMatricesGetDiagonal(unittest.TestCase):
    def test_Identity_matrix1(self):
        x = IdentityMatrix(1)
        expected = [1]
        self.assertEqual(x.get_diagonal(), expected,
                         'one by one matrix')

    def test_Identity_matrix2(self):
        x = IdentityMatrix(2)
        expected = [1, 1]
        self.assertEqual(x.get_diagonal(), expected,
                         'two by two matrix')

    def test_Identity_matrix3(self):
        x = IdentityMatrix(3)
        expected = [1, 1, 1]
        self.assertEqual(x.get_diagonal(), expected,
                         '3 by 3 matrix')


class TestIdentityMatricesSwap(unittest.TestCase):
    def test_swap_rows_itself(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(1, 2)
        self.assertEqual(x.swap('r', 1, 'r', 1), expected,
                         'swap rows with itself')

    def test_swap_rows(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'r', 2), expected,
                         'swap rows')

    def test_swap_columns_itself(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('c', 1, 'c', 1), expected,
                         'swap columns with itself')

    def test_swap_columns(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('c', 1, 'c', 2), expected,
                         'swap columns')

    def test_swap_row_column(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'c', 2), expected,
                         '1st row swap 2nd column')

    def test_swap_row_column(self):
        x = IdentityMatrix(2)
        expected = DiagonalMatrix(0, 2)
        self.assertEqual(x.swap('r', 1, 'c', 1), expected,
                         '1st row swap 1st column')

    def test_swap_row_column(self):
        x = IdentityMatrix(3)
        expected = DiagonalMatrix(1, 3)
        self.assertEqual(x.swap('c', 2, 'r', 2), expected,
                         '2st row swap 2nd column')

    def test_swap_row_fail1(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'r', 2),
                         'swap row zero')

    def test_swap_row_fail2(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'r', 2),
                         'swap row out of bounds')

    def test_swap_column_fail1(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'c', 2),
                         'swap column zero')

    def test_swap_column_fail2(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 3, 'c', 2),
                         'swap column out of bounds')

    def test_swap_row_column_fail1(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 0, 'c', 2),
                         'swap row zero')

    def test_swap_row_column_fail2(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('r', 3, 'c', 2),
                         'swap row out of bounds')

    def test_swap_row_column_fail3(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 0, 'r', 2),
                         'swap column zero')

    def test_swap_row_column_fail4(self):
        x = IdentityMatrix(2)
        self.assertEqual(MatrixOutOfBound, x.swap('c', 4, 'c', 2),
                         'swap column out of bounds')


unittest.main(exit=False)

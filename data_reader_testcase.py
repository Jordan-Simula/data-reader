import unittest
from data_reader import read_arff
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_first_row(self):
        numpy_array = read_arff('auto_mpg.arff')
        np.testing.assert_array_equal(numpy_array[0], [b'18.0', b'8', b'307.0', b'130.0', b'3504.0', b'12.0', b'70.0', b'NorthAmerica',
 b'chevrolet chevelle malibu'])

    def test_last_row(self):
        numpy_array = read_arff('auto_mpg.arff')
        np.testing.assert_array_equal(numpy_array[-1],
                                      [b'31.0', b'4', b'119.0', b'82.0', b'2720.0', b'19.4', b'82.0', b'NorthAmerica',
                                       b'chevy s-10'])

    def test_shape(self):
        numpy_array = read_arff('auto_mpg.arff')
        np.testing.assert_equal(numpy_array.shape, (398,9))


if __name__ == '__main__':
    unittest.main()

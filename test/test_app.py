from src.app import _datetime_obj2string #add import *
import datetime
import unittest

class TestApp(unittest.TestCase):
    # Tests
    # 01
    def test_datetime_obj2string(self):
        test_input = datetime.datetime(2021, 7, 14, 20, 46, 3)
        expected_output = '20210714T204603Z'
        actual_output = _datetime_obj2string(test_input)
        self.assertEqual(expected_output, actual_output)

    #02
    def test_validate_t2_greater_than_t1(self):
        pass



if __name__ == '__main__':
    unittest.main()
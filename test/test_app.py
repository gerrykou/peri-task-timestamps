import datetime
import unittest
import src.app as app
#from src.app import _datetime_obj2string
#from src.app import *
#import _validate_t2_greater_than_t1 #add import *


class TestApp(unittest.TestCase):
    # Tests
    # 01
    def test_datetime_obj2string(self):
        test_input = datetime.datetime(2021, 7, 14, 20, 46, 3)
        expected_output = '20210714T204603Z'
        actual_output = app._datetime_obj2string(test_input)
        self.assertEqual(expected_output, actual_output)

    #02
    def test_validate_t2_greaterorequal_than_t1(self):
        test_input_time1 ='20211115T123456Z'
        test_input_time2 = '20180214T204603Z'
        with self.assertRaises(SystemExit):
            app._validate_t2_greaterorequal_than_t1(test_input_time1,test_input_time2)


if __name__ == '__main__':
    unittest.main()
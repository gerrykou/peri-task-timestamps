import datetime
import pytest
import src.app as app

#01
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

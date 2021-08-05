from src.app import *
import unittest

class TestApp(unittest.TestCase):

    # Test 'Parse arguments'
    # 01
    def test_parse_args(self):
        test_input = '--period=1h --tz=Europe/Athens --t1=20210714T204603Z --t2=20210715T123456Z'
        expected_output = '''"20210714T210000Z"\n"20210714T220000Z"\n"20210714T230000Z"\n"20210715T000000Z"\n"20210715T010000Z"
        #"20210715T020000Z"\n"20210715T030000Z"\n"20210715T040000Z"\n"20210715T050000Z"\n
        #"20210715T060000Z"\n"20210715T070000Z"\n"20210715T080000Z"\n"20210715T090000Z"\n
        #"20210715T100000Z"\n"20210715T110000Z"\n"20210715T120000Z"'''
        actual_output = parse_args(test_input)

        self.assertEqual(expected_output, actual_output)

    def test_validate_datetime(self):
        test_input = '--period=1h --tz=Europe/Athens --t1=20210714T204603Z --t2=20210715T123456Z'
        expected_output = '''"20210714T210000Z"\n"20210714T220000Z"\n"20210714T230000Z"\n"20210715T000000Z"\n"20210715T010000Z"
        #"20210715T020000Z"\n"20210715T030000Z"\n"20210715T040000Z"\n"20210715T050000Z"\n
        #"20210715T060000Z"\n"20210715T070000Z"\n"20210715T080000Z"\n"20210715T090000Z"\n
        #"20210715T100000Z"\n"20210715T110000Z"\n"20210715T120000Z"'''
        actual_output = parse_args(test_input)

        self.assertEqual(expected_output, actual_output)

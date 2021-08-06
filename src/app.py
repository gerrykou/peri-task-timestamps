#!/usr/bin/env python3
from pyfiglet import Figlet
import argparse, sys, datetime, pytz
from dateutil.relativedelta import relativedelta

VAR_CHOICES={'1h':'hours=+1', '1d':'days=+1', '1mo':'months=+1', '1y':'years=+1'}
FORMAT = "%Y%m%dT%H%M%SZ"
def show_title():
    """Show the program title
    """
    f = Figlet(font='standard')
    print(f.renderText('peri task timestamps'))

def parse_args():
    parser = argparse.ArgumentParser( description = 'Print periodic tasks timestamps')
    parser.add_argument("--period", metavar='', type=str, required=True, help="The supported periods are: 1h, 1d, 1mo, 1y.")
    parser.add_argument("--t1",metavar='', required=True, help="t1 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--t2",metavar='', required=True, help="t2 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--tz",metavar='', type=str, required=True, help="timezone e.g --tz=Europe/Athens ,see http://pytz.sourceforge.net/ and https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('-v','--verbose', action='store_true', default=False, help="increase the verbosity level")
    output = parser.parse_args()
    
    if output.period not in VAR_CHOICES.keys():
        print("ERROR: Unsupported period")
        exit(10)

    _validate_timezone(output.tz)

    date_list=[output.t1,output.t2]
    for input_date in date_list:
        _validate_datetime(input_date) 

    _validate_t2_greater_than_t1(output.t1,output.t2)
    _validate_period(output.period)

    return output


def _validate_timezone(input_timezone):
    if input_timezone not in pytz.all_timezones:
        print('ERROR: Invalid timezone string!')
        exit(10)

def _validate_t2_greater_than_t1(time1,time2):
    if time1 > time2:
        print('ERROR: t2 must be greater than t1')
        exit(10)


def _validate_datetime(input_date):
    try:
        date_object=datetime.datetime.strptime(input_date, FORMAT)
        return date_object
    except:
        print("ERROR: This is not a correct date string format. It should be YYYYMMDDTHHMMSSZ, try --help for more info")
        exit(10)

def _validate_period(period):
    if period not in VAR_CHOICES:
        print('ERROR: Unsupported period')
        exit(10)

def _datetime_str2obj(input_date):
        date_obj=datetime.datetime.strptime(input_date, FORMAT)
        return date_obj


def _datetime_obj2string(input_date):
        date_obj=datetime.datetime.strftime(input_date, FORMAT)
        return date_obj


def create_timestamps_list(time1, time2, period):
    #add period to timestamp, to be improved to read values from dictionary VAR_CHOICES.values()
    print(VAR_CHOICES[period])
    #while time1 < time2:
    print(time1<time2)
    if period == '1h':
        new_timestamp=(time1 + relativedelta(hours=+1))
    if period == '1d':
        new_timestamp=(time1 + relativedelta(days=+1))
    if period == '1mo':
        new_timestamp=(time1 + relativedelta(months=+1))
    if period == '1y':
        new_timestamp=(time1 + relativedelta(years=+1))
    # utc_dt = datetime.datetime.strftime(dt, FORMAT)
    return _datetime_obj2string(new_timestamp)


def main():
    #show_title()
    args = parse_args()
    PERIOD = args.period
    T1 = args.t1
    T2 = args.t2
    TZ = args.tz
    #print (PERIOD,T1,T2,TZ)
    #timevar=datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    #print(timevar)

    T1_obj =_datetime_str2obj(T1)
    T2_obj =_datetime_str2obj(T2)
    print(T1_obj)
    print(create_timestamps_list(T1_obj, T2_obj, PERIOD))
    while True:
        try:
            print("Program arguments:")
            print(args)
            sys.exit(0)
        except ValueError:
            print('ERROR: Unsupported arguments')
            exit(10)

    
if __name__ == "__main__":
    main()
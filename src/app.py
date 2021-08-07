#!/usr/bin/env python3
from pyfiglet import Figlet
import argparse, datetime, pytz, timedelta, calendar
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
    output = parser.parse_args()

    _validate_timezone(output.tz)

    date_list=[output.t1,output.t2]
    for input_date in date_list:
        _validate_datetime(input_date) 

    _validate_t2_greaterorequal_than_t1(output.t1,output.t2)
    _validate_period(output.period)

    return output


def _validate_timezone(input_timezone):
    if input_timezone not in pytz.all_timezones:
        print('ERROR: Invalid timezone string, try --help for more info')
        exit(10)


def _validate_datetime(input_date):
    try:
        date_object=datetime.datetime.strptime(input_date, FORMAT)
        return date_object
    except:
        print("ERROR: This is not a correct date string format. It should be YYYYMMDDTHHMMSSZ, try --help for more info")
        exit(10)


def _validate_t2_greaterorequal_than_t1(time1,time2):
    time1_obj= _datetime_str2obj(time1)
    time2_obj= _datetime_str2obj(time2)
    if time1_obj >= time2_obj:
        print('ERROR: t2 must be greater than t1')
        exit(10)


def _validate_period(period):
    if period not in VAR_CHOICES:
        print('ERROR: Unsupported period')
        exit(10)


def _datetime_str2obj(input_time):
    time_obj=datetime.datetime.strptime(input_time, FORMAT)
    return time_obj


def _datetime_obj2string(input_time):
    time_obj=datetime.datetime.strftime(input_time, FORMAT)
    return time_obj

def _create_aware_time_object(naive_time_obj):
    #creates aware time objects assigning +00:00 for utc
    aware_time_obj = naive_time_obj.replace(tzinfo=pytz.UTC)
    return aware_time_obj

# def _increment_time_delta(time,period):
#     #time needs to be object
#     #add period to time, to be improved to read values from dictionary VAR_CHOICES.values()
#     #output is in timestamp format

#     if period == '1h':
#         new_timestamp=(time + datetime.timedelta(hours=1))
#     if period == '1d':
#         new_timestamp=(time + datetime.timedelta(days=1))
#     if period == '1mo':
#         new_timestamp=(time + datetime.timedelta(months=1))
#     if period == '1y':
#         new_timestamp=(time + datetime.timedelta(years=1))
#     output = new_timestamp
#     return output

def _increment_time_f(time,period):
    #time needs to be object
    #add period to time, to be improved to read values from dictionary VAR_CHOICES.values()
    #output is in timestamp format

    if period == '1h':
        new_time_obj=(time + relativedelta(hours=+1))
        #new_timestamp=(time + datetime.timedelta(hours=1))
    if period == '1d':
        new_time_obj=(time + relativedelta(days=+1))
        #new_timestamp=(time + datetime.timedelta(days=1))
    if period == '1mo':
        #last_day=calendar.monthrange(aware_time_obj.year, aware_time_obj.month)[1]
        #new_time_obj=(time + relativedelta(months=+1))
        plus_month_time_obj=(time + relativedelta(months=+1))
        this_month=plus_month_time_obj.month
        this_year=plus_month_time_obj.year
        last_day=calendar.monthrange(this_year, this_month)[1]
        new_time_obj=plus_month_time_obj.replace(second=0, microsecond=0, minute=0, hour=plus_month_time_obj.hour, day = last_day)
    if period == '1y':
        new_time_obj=(time + relativedelta(years=+1))
    output = new_time_obj
    return output



def _utc_to_local_time_object(aware_time_obj,local_tz):
    #not used here, in case tranformation from utc to local timezone time is needed to calculate Daylight Saving time
    #timezone=pytz.timezone(TZ)
    loc_tmz = pytz.timezone(local_tz)
    local_time_obj=aware_time_obj.astimezone(loc_tmz)
    return local_time_obj


def _datetime_to_utc(time_obj):
    #not used here, in case tranformation from local timezone to utc is needed
    utc_time_obj =time_obj.astimezone(pytz.utc)
    return utc_time_obj


def round_time_object(time_obj,period):
    if period == '1h':
        #round time objects to hour e.g rounds 2021-10-10 20:46:03 to 2021-10-10 20:00:00 
        output = time_obj.replace(second=0, microsecond=0, minute=0, hour=time_obj.hour)
    if period == '1d':
        #round time objects hour and day to include also the same day in timestamps e.g rounds 2021-10-10 20:46:03 to 2021-10-09 20:00:00 
        output = time_obj.replace(second=0, microsecond=0, minute=0, hour=time_obj.hour, day = time_obj.day-1)
    if period == '1mo':
        #round time objects to hour e.g rounds 2021-10-10 20:46:03 to 2021-10-10 20:00:00 
        output = time_obj.replace(second=0, microsecond=0, minute=0, hour=time_obj.hour, month= time_obj.month-1)
    if period == '1y':
        #round time objects to hour and last day in previous year  
        output = time_obj.replace(second=0, microsecond=0, minute=0, hour=time_obj.hour, year = time_obj.year-1, day = 31, month =12)
    return output


def create_timestamps_list(time1_obj, time2_obj, period, timezone):
    #time1 and time2 need to be objects
    incremented_time = time1_obj
    count =0 
    output_list=[]
  
    while incremented_time < time2_obj:
        incremented_time = _increment_time_f(incremented_time,period)

        timestamp_incremented=_datetime_obj2string(incremented_time)

        output_list.append(timestamp_incremented)

        count += 1
        if count >= 100:
            #break in case of infite loop
            print('ERROR: Loop terminated after %s iterations' % count)
            break
    
    print(output_list)
    return output_list


def main():
    show_title()
    while True:
        try:
                args = parse_args()
                print("Program arguments:", args)

                PERIOD = args.period
                T1 = args.t1
                T2 = args.t2
                TZ = args.tz

                naive_T1_obj =_datetime_str2obj(T1)
                naive_T2_obj =_datetime_str2obj(T2)

                aware_T1_obj= _create_aware_time_object(naive_T1_obj)
                aware_T2_obj= _create_aware_time_object(naive_T2_obj)

                rounded_T1_obj=round_time_object(aware_T1_obj,PERIOD)
                rounded_T2_obj=round_time_object(aware_T2_obj,PERIOD)
                create_timestamps_list(rounded_T1_obj, rounded_T2_obj, PERIOD, TZ)
                exit(0)
        except ValueError:
            print('ERROR: Unsupported arguments')
            exit(10)


    
if __name__ == "__main__":
    main()
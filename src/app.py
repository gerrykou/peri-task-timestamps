#!/usr/bin/env python3
from pyfiglet import Figlet
import argparse
import sys

VAR_CHOICES={'1h' : 'an hour', '1d':'a day', '1mo':'a month', '1y':'a year'}

def show_title():
    """Show the program title
    """
    f = Figlet(font='standard')
    print(f.renderText('peri task timestamps'))

def parse_args():
    parser = argparse.ArgumentParser(description = 'Print periodic tasks timestamps')
    parser.add_argument("--period", metavar='', required=True, choices=VAR_CHOICES.keys(), help="The supported periods are: 1h, 1d, 1mo, 1y.")
    parser.add_argument("--t1",metavar='', required=True, help="t1 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--t2",metavar='', required=True, help="t2 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--tz",metavar='', required=True, help="timezone e.g --tz=Europe/Athens")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v','--verbose', action='store_true', default=False, help="increase the verbosity level")
    output = parser.parse_args()
    return output
    
def main():
    show_title()
    args = parse_args()
    #PERIOD = args.period
    #T1 = args.t1
    #T2 = args.t2
    #TZ = args.tz
    #print (PERIOD,T1,T2,TZ)
    if args.verbose:
        try:
            print("Program arguments:")
            print(args)
            sys.exit(0)
        except:
            sys.stderr.write("spam\n")
            sys.exit(10)


    
    

    
if __name__ == "__main__":
    main()
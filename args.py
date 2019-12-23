import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start-date', help = 'specify the date to crawl from YYYY-MM-DD', required = True)
    parser.add_argument('-e', '--end-date', help = 'specify the date to crawl until YYYY-MM-DD', required = True)
    parser.add_argument('-o', '--output', help = 'specify the output file name', default = 'output.csv')

    args = parser.parse_args()
    args.start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    args.end_date = datetime.strptime(args.end_date, "%Y-%m-%d")

    return args

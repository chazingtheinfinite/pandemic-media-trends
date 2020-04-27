""" File: compare-concept.py
Author: Kevin Dick
Date: 2020-04-26
---
Description: Compares the TV-AI news coverage volume for a specific keyword/topic
with respect to the pandemmic, an equivalently sized window in time pre-pandemic,
and with a randomly selected subset of equvalently sized, contiguous, and non-overlapping
set of windows. 
"""
import datetime
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-q', '--query', required=True,
                    help='query word to perform analysis')
parser.add_argument('-o', '--outpu_file', required=True,
                    help='csv file to which the results are appended')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase verbosity')
args = parser.parse_args()

# EXAMPLE: python3 compare_concept.py -q kindness -o global-trends.csv -v

PANDEMIC_START = '20200211000000'
GDELT_BASE     = 'https://api.gdeltproject.org/api/v2/tvai/tvai?format=html'

def get_pandemic_dates():
	""" get_pandemic_dates
	    Returns the start and end dates in string format for the current pandemic period.
	    Input: None
	    Output: <dict>, start date and end date
	"""
	return {'start' : PANDEMIC_START, 'end' : datetime.datetime.now().strftime("%Y%m%d") + '235959'} # The very end of today

def get_url(dates):
	"""get_url
	   Returns the url of the csv containing the normalised airtime coverage for the query.
	   Input: <dict> dates, the start and end dates
	   Output: <str>, the url to the csv data of the keyword coverage over the specified dates.
	"""
	return '{}&startdatetime={}&enddatetime={}&dateres=DAY&query=%20cap:%22{}%22%20%20(station:KGO%20OR%20station:KPIX%20OR%20station:KNTV%20OR%20station:CNN%20OR%20station:MSNBC%20OR%20station:FOXNEWS%20OR%20station:BBCNEWS%20)%20&mode=timelinevolstream&timezoom=yes&format=csv'.format(GDELT_BASE, dates['start'], dates['end'], args.query)

def get_prepandemic_dates(pd):
	""" get_prepandemic_dates
	    Counts the number of days in the pandemic dates to obtain equivalently sized pre-pandemic dates.
	    Input: <dict> pd
	    Output: <dict>, start date and end date
	"""
	pan_end   = datetime.date(int(pd['end'][0:4]), int(pd['end'][4:6]), int(pd['end'][6:8]))
	pan_start = datetime.date(int(pd['start'][0:4]), int(pd['start'][4:6]), int(pd['start'][6:8]))
	start_date  = pan_start - datetime.timedelta(days=abs(pan_end - pan_start).days)
	return {'start' : start_date.strftime("%Y%m%d") + '000000', 'end': PANDEMIC_START}

def get_random_prepan_dates():
	""" get_random_prepan_dates
	
	"""
	# Count the number of days between start-prepandemic and July 6th, 2010
	# Subtract window_soze from it
	# Randomly select 100 numbers from it
	# Use those numbers, subtracted from end-date to "seed" each contigious window
	# add to a list of os windows to extract from.

def main():
	""" main function """
	pandemic_dates = get_pandemic_dates()
	prepan_dates   = get_prepandemic_dates(pandemic_dates)
	if args.verbose: print('Pandemic Dates: {}\nPrePandemic Dates: {}'.format(pandemic_dates, prepan_dates))
	
	pan_url    = get_url(pandemic_dates)
	prepan_url = get_url(prepan_dates)
	if args.verbose: print('PanUrl: {}\nPrePanUrl: {}'.format(pan_url, prepan_url))

if __name__ == "__main__": main()

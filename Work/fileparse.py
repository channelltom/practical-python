# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter = ',',silence_errors=False):
	'''
	Parse a CSV file into a list of records
	'''
	if select and not has_headers:
		raise RuntimeError('Select argument requires column headers.')
	
	
	rows = csv.reader(lines, delimiter=delimiter)

	# Read the file headers
	#if has_headers == True: #My Code#
	#headers = next(rows)
	headers = next(rows) if has_headers else [] #Solution given#
	
	# If specific columns have been selected, make indices for filtering.
	if select:
		indices = [ headers.index(colname) for colname in select ]
		headers = select
	else:
		indices = []

	records = []
	for rownum, row in enumerate(rows, 1):
		if not row:
			continue
		
		if select:
			row = [ row[index] for index in indices ]

		if types:
			try:
				row = [ func(val) for func, val in zip(types, row) ]
			except ValueError as e:
				if not silence_errors:
					print(f'Row {rownum}: Could not convert {row}')
					print(f'Row {rownum}: Reason {e}')
				continue
		if has_headers == True:
			record = dict(zip(headers, row))
		else:
			record = tuple(row)
		records.append(record)

	return records

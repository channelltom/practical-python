# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types = None, has_headers=True, delimiter = ','):
	'''
	Parse a CSV file into a list of records
	'''
	
	with open(filename) as f:
		rows = csv.reader(f, delimiter=delimiter)

		# Read the file headers
#		if has_headers == True: #My Code#
#			headers = next(rows)
		headers = next(rows) if has_headers else [] #Solution given#
		
		# If specific columns have been selected, make indices for filtering.
		if select:
			indices = [ headers.index(colname) for colname in select ]
			headers = select
		else:
			indices = []

		records = []
		for row in rows:
			if not row:
				continue
			
			if select:
				row = [ row[index] for index in indices ]

			if types:
				row = [ func(val) for func, val in zip(types, row) ]

			if has_headers == True:
				record = dict(zip(headers, row))
			else:
				record = tuple(row)
			records.append(record)

	return records

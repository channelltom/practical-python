# report.py
#
# Exercise 2.4

import csv
import fileparse
from stock import Stock

def read_portfolio(filename):
	'''
	Read a stock portfolio into a list of dictionaries with keys
	name, shares and price.
	'''
	with open(filename) as lines:
		portdicts =  fileparse.parse_csv(lines, select=['name', 'shares','price'], types=[str, int, float])
	portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
	return portfolio

def read_prices(filename):
	'''
	Read a CSV file of price data into a dict mapping names to prices.
	'''
	with open(filename) as lines:
		return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
	'''
	Make a list of (name, shares, price, change) tuples given a portfolio list
	and prices dictionary
	'''
	rows = []
	for s in portfolio:
		current_price = prices[s.name]
		change = current_price - s.price
		summary = (s.name, s.shares, current_price, change)
		rows.append(summary)
	return rows

def print_report(reportdata):
	headers = ('Name', 'Shares', 'Price', 'Change')
	print('%10s %10s %10s %10s' % headers)
	print(('-' * 10 + ' ') * len(headers))
	for row in reportdata:
		print('%10s %10s %10.2f %10.2f' % row)


def portfolio_report(portfolio_filename, prices_filename):
	'''
	Function to execute the printing of the final report.
	'''
	# Collate data from csv files.
	portfolio = read_portfolio(portfolio_filename)
	prices = read_prices(prices_filename)

	# Create report data.
	report = make_report_data(portfolio, prices)

	# Print out report data.
	print_report(report)

def main(args):
	if len(args) != 3:
		raise SystemExit('Usage: %s portfile pricefile' % args[0])
	portfolio_report(args[1], args[2])

if __name__ == '__main__':
	import sys
	main(sys.argv)
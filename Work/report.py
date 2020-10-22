import csv
from fileparse import parse_csv


def read_portfolio(filename):
	'''
	Read a stock portfolio into a list of dictionaries with keys
	name, shares and price.
	'''
	portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])
	return portfolio

def read_prices(filename):
	'''
	Read a CSV file of price data into a dict mapping names to prices.
	'''
	prices = dict(parse_csv(filename, types=[str, float], has_headers=False))
	return prices


def make_report_data(portfolio, prices):
	'''
	Make a list of (name, shares, price, change) tuples given a portfolio list
	and prices dictionary
	'''

	rows = []
	for stock in portfolio:
		current_price = prices[stock['name']]
		change = current_price - stock['price']
		summary = (stock['name'], stock['shares'], current_price, change)
		rows.append(summary)
	return rows

def print_report(report):
	headers = ('Name', 'Shares', 'Price', 'Change')
	print('%10s %10s %10s %10s' % headers)
	print(('-' * 10 + ' ') * len(headers))
	for row in report:
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


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')


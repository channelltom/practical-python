# pcost.py
#
# Exercise 1.27

import csv
import report
import sys
from stock import Stock

def portfolio_cost(filename):
    ''' 
    Computes the total cost (shares*price) of a portfolio file.
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s.cost() for s in portfolio])

#if len(sys.argv) == 2:
#    filename = sys.argv[1]
#else:
#    filename = input('Enter a filename: ')

def main(args):
    if len(args) != 2:
        SystemExit('Usage: %s portfile' % args[0])
    cost = portfolio_cost(args[1])
    print('Total Cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
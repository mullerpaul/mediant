#!/usr/bin/env python3

import argparse

# global variables for size of board and the board itself

# helper functions
def print_fraction(numerator, denominator):
	print (numerator + '/' + denominator)

# main
def main():
	parser = argparse.ArgumentParser(description='Compute the mediant of two fractions')
	parser.add_argument('fraction_a_num', help='Numerator of the first fraction')
	parser.add_argument('fraction_a_dem', help='Denominator of the first fraction')
	parser.add_argument('fraction_b_num', help='Numerator of the second fraction')
	parser.add_argument('fraction_b_dem', help='Denominator of the second fraction')

	args = parser.parse_args()

	#debug - print inputs
	print_fraction(args.fraction_a_num, args.fraction_a_dem)
	print_fraction(args.fraction_b_num, args.fraction_b_dem)

	# check for valid inputs:
	#	only positive integers
	#	no zero denominators
	#if args.fraction_a_dem == 0 or args.fraction_b_dem == 0:
	#	print('denominators cannot be zero')

	#if args.fraction_a_dem < 0 OR args.fraction_a_num < 0 OR args.fraction_b_dem < 0 OR args.fraction_b_num < 0:
	#	print('no negative numbers')


# need this to make this run from command line
if __name__ == '__main__':
	main()




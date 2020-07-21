#!/usr/bin/env python3

import argparse

# helper functions
def print_fraction(label, numerator, denominator):
	print (label + ' ' + str(numerator) + '/' + str(denominator))

# actual process
def compute_mediant(a, b, c, d):
	return (a + c), (b + d);

# main
def main():
	parser = argparse.ArgumentParser(description='Compute the mediant of two fractions')
	parser.add_argument('fraction_a_num', type=int, help='Numerator of the first fraction')
	parser.add_argument('fraction_a_dem', type=int, help='Denominator of the first fraction')
	parser.add_argument('fraction_b_num', type=int, help='Numerator of the second fraction')
	parser.add_argument('fraction_b_dem', type=int, help='Denominator of the second fraction')

	args = parser.parse_args()

	#debug - print inputs
	print_fraction("first fraction", args.fraction_a_num, args.fraction_a_dem)
	print_fraction("second fraction", args.fraction_b_num, args.fraction_b_dem)

	# check for valid inputs no zero denominators and only positive integers
	if args.fraction_a_dem == 0 or args.fraction_b_dem == 0:
		print('error: denominators cannot be zero')
		quit()
	if args.fraction_a_dem < 0 or args.fraction_a_num < 0 or args.fraction_b_dem < 0 or args.fraction_b_num < 0:
		print('no negative numbers')
		quit()

	result_num, result_dem = compute_mediant(args.fraction_a_num, args.fraction_a_dem, args.fraction_b_num, args.fraction_b_dem)
	print_fraction("mediant", result_num, result_dem)


# need the following to make this run from command line
if __name__ == '__main__':
	main()




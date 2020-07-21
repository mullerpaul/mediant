#!/usr/bin/env python3

import argparse

# helper functions
def print_debug(index, numerator, denominator, decimal):
	print (f"Iteration: {index}  Approximation: {numerator}/{denominator}  Decimal value: {decimal}")

# actual process
def compute_mediant(a, b, c, d):
	return (a + c), (b + d);

# main
def main():
	parser = argparse.ArgumentParser(description='Compute a fractional approximation to a decimal number')
	parser.add_argument('target', type=float, help='Number to approximate')

	args = parser.parse_args()
	target = args.target

	#debug - print inputs
	#print(f"target number {target}")

	# check for valid input : decimal number between 0 and 1
	if target < 0 or target > 1:
		print('error: number must be between 0 and 1')
		quit()

	iteration = 1
	lower_num = 0
	lower_dem = 1
	higher_num = 1
	higher_dem = 1
	result_decimal = 0.0
	while (iteration < 11 and result_decimal != target):
		result_num, result_dem = compute_mediant(lower_num, lower_dem, higher_num, higher_dem)
		result_decimal = result_num/result_dem
		print_debug(iteration, result_num, result_dem, result_decimal)
		if target > result_decimal:
			#print("approximation is too low")
			lower_num = result_num
			lower_dem = result_dem
		else:
			#print("approximation is too high")
			higher_num = result_num
			higher_dem = result_dem

		iteration = iteration + 1

	print()
	print(f"Target: {target}  Approximation: {result_num}/{result_dem}  Decimal value: {result_decimal}  Error: " + str(abs(result_decimal - target)))


# need the following to make this run from command line
if __name__ == '__main__':
	main()


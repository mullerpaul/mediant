# python implementation of a function which computes the mediant of a pair of fractions

See the wikipedia page for more information about the mediant function
https://en.wikipedia.org/wiki/Mediant_(mathematics)

There are two executables in this repo.
mediant.py is where I got the function working.  It simply accepts two fractions as input and returns the mediant.
fractional_approximation.py is the interesting one where you enter a decimal (0,1) and the program will iteratively split the range using the mediant to come up with better and better approximations to the inputted number.

Both are meant to be run from the command line and both use positional parameters as inputs.
Use the -h flag to see the usage information.

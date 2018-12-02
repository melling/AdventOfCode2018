"""
Part 1 Solution: 580
Part 2 Solution: 81972
"""

# Basically a Sum function

def solve_day1_part1():
	fname = "data_day1.txt"
	frequency = 0

	with open(fname) as fp:
		line = fp.readline().rstrip("\n")
		while line:
			i = int(line)
			frequency += i
			# print("{} => {} = {}".format(line, i, total))
			# print("{}".format(frequency))

			line = fp.readline().rstrip("\n")
	return frequency

"""
# Notes
- Must read the data several times until we find a repeated frequency.
- Maybe I should read the data in a list once for performance but what if we have billions of numbers?
"""

def solve_day1_part2(frequency, frequency_count):
	fname = "data_day1.txt"

	# total_count["-17"] = 3
	with open(fname) as fp:
		line = fp.readline().rstrip("\n")
		while line:
			i = int(line)
			frequency += i
			key = str(frequency)
			
			if key not in frequency_count:
				frequency_count[key] = 1
				# print("Adding T={}\n".format(key))
			else:
				print("Dup T={}".format(key))
				# print("Frequency table: 1".format(total_count))
				return key
			# print("{} => {} = {}".format(line, i, total))
			line = fp.readline().rstrip("\n")
	# print("Once more")
	return solve_day1_part2(frequency, frequency_count)

total = solve_day1_part1()
print("Sum={}".format(total))


# frequency_count = {}
first_repeat = solve_day1_part2(0, {})
print("first repeated ={}".format(first_repeat))

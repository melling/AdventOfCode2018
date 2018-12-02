# python3

"""
Part 1 Solution: 247 x 25 = 6175

"""

def read_data(fname):
	lines = []
	with open(fname) as fp:
		line = fp.readline().rstrip("\n")
		while line:
			lines.append(line)
			line = fp.readline().rstrip("\n")

	return lines


def checkId(id):
	letter_count = {}

	for letter in id:
		#print(letter)
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] += 1
	
	hasExactly2 = False
	hasExactly3 = False
			
	for k, v in letter_count.items():
		#print("{} = {}".format(k,v))
		
		if v == 2:
			hasExactly2 = True
		elif v == 3:
			hasExactly3 = True
			
	return hasExactly2, hasExactly3	
	

def solve_day2_part1(box_ids):
	num2 = 0
	num3 = 0
		
	for id in box_ids:
		exactly2, exactly3 = checkId(id)
		#print("id={}, Match={}".format(id, exactly2))
		if exactly2:
			num2 += 1
		if exactly3:
			num3 += 1

	print("{} x {} = {}".format(num2, num3, num2*num3))
	

def cmp_strings(str1, str2):
	differences = 0

	for i in range(len(str1)):
		if str1[i] != str2[i]:
			differences += 1

	return differences


def solve_day2_part2(box_ids):
	num2 = 0
	num3 = 0
	n_box_ids = len(box_ids) - 1
	print("Number boxes: {}".format(n_box_ids))

	for i in range(0, n_box_ids):
		str1 = box_ids[i]

		# letters1 = 
		for j in range(i, n_box_ids+1):
			str2 = box_ids[j]
			# print("{}, {} Comparing={}, {}".format(i, j, str1, str2))
			n = cmp_strings(str1, str2)
			if n == 1:
				print("{}, {} Comparing={}, {}".format(i, j, str1, str2))

	# print("{} x {} = {}".format(num2, num3, num2*num3))
	
# solve_day2(["bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"])
data_day2 = read_data("data_day2.txt")
solve_day2_part1(data_day2)

solve_day2_part2(data_day2)
n = cmp_strings("abc", "abc")
n = cmp_strings("abc", "abe")
n = cmp_strings("xbc", "abc")
n = cmp_strings("xbc", "adc")

# print("differences={}".format(n))
# print(data)

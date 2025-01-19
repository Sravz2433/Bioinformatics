# Python program to find Burrows-Wheeler Transform of a given text
# Compares the rotations and sorts the rotations alphabetically


def cmp_func(x, y):
	return (x[1] > y[1]) - (x[1] < y[1])

# Takes text to be transformed and its length as arguments
# and returns the corresponding suffix array


def compute_suffix_array(input_text, len_text):
	# Array of structures to store rotations and their indexes
	suff = [(i, input_text[i:]) for i in range(len_text)]

	# Sorts rotations using comparison function defined above
	suff.sort(key=lambda x: x[1])

	# Stores the indexes of sorted rotations
	suffix_arr = [i for i, _ in suff]

	# Returns the computed suffix array
	return suffix_arr

# Takes suffix array and its size as arguments
# and returns the Burrows-Wheeler Transform of given text


def find_last_char(input_text, suffix_arr, n):
	# Iterates over the suffix array to
	# find the last char of each cyclic rotation
	bwt_arr = ""
	for i in range(n):
		# Computes the last char which is given by 
		# input_text[(suffix_arr[i] + n - 1) % n]
		j = suffix_arr[i] - 1
		if j < 0:
			j = j + n
		bwt_arr += input_text[j]

	# Returns the computed Burrows-Wheeler Transform
	return bwt_arr


# Driver program to test functions above
input_text = "GATTGCTTTT$"
len_text = len(input_text)

# Computes the suffix array of our text
suffix_arr = compute_suffix_array(input_text, len_text)

# Adds to the output array the last char of each rotation
bwt_arr = find_last_char(input_text, suffix_arr, len_text)

print("Input text :", input_text)
print("Burrows - Wheeler Transform :", bwt_arr)


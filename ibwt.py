# Python program for the above approach

import string

# Structure to store info of a node of linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Does insertion at end in the linked list
def addAtLast(head, nn):
	if head is None:
		head = nn
		return head
	temp = head
	while temp.next is not None:
		temp = temp.next
	temp.next = nn
	return head

# Computes l_shift[]
def computeLShift(head, index, l_shift):
	l_shift[index] = head.data
	head = head.next

# Compares the characters of bwt_arr[] and sorts them alphabetically
def cmpfunc(a, b):
	return ord(a) - ord(b)

def invert(bwt_arr):
	len_bwt = len(bwt_arr)
	sorted_bwt = sorted(bwt_arr)
	l_shift = [0] * len_bwt

	# Index at which original string appears
	# in the sorted rotations list
	x = 4

	# Array of lists to compute l_shift
	arr = [[] for i in range(128)]

	# Adds each character of bwt_arr to a linked list
	# and appends to it the new node whose data part
	# contains index at which character occurs in bwt_arr
	for i in range(len_bwt):
		arr[ord(bwt_arr[i])].append(i)

	# Adds each character of sorted_bwt to a linked list
	# and finds l_shift
	for i in range(len_bwt):
		l_shift[i] = arr[ord(sorted_bwt[i])].pop(0)

	# Decodes the bwt
	decoded = [''] * len_bwt
	for i in range(len_bwt):
		x = l_shift[x]
		decoded[len_bwt-1-i] = bwt_arr[x]
	decoded_str = ''.join(decoded)

	print("Burrows - Wheeler Transform:", bwt_arr)
	print("Inverse of Burrows - Wheeler Transform:", decoded_str[::-1])

# Driver program to test functions above
if __name__ == "__main__":
	bwt_arr = "AT$AAACTTCG"
	invert(bwt_arr)

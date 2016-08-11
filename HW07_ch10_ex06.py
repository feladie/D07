# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(t):
	"""Returns true if the list is sorted.
	"""
	copy = list(t)
	copy.sort()
	for index in range(len(t)):
		if t[index] != copy[index]:
			return False
	return True 

def main():
	# print(is_sorted([1, 2, 3]))
	# print(is_sorted([3, 2, 1]))
	# print(is_sorted(['a', 'b']))
	# print(is_sorted(['b', 'a']))
	pass

if __name__ == '__main__':
	main()

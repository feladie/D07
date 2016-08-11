# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(t):
	"""Capitalizes all strings within a nested list
	"""
	res = [] # resulting list
	for s in t: # for each item in list
		if isinstance(s, str): # if string
			res.append(s.capitalize())
		else: # if list 
			res.append(capitalize_nested(s))
	return res


def main():
	# print(capitalize_nested(['anna', 'anthony', 'andrew']))
	# print(capitalize_nested([['anna', 'anthony', ['angel']], 'andrew']))
	...

if __name__ == '__main__':
	main()

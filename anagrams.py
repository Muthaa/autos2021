# 1.sorted method
def check1(s1, s2):
     
	# the sorted strings are checked
	if(sorted(s1)== sorted(s2)):
	    print("The strings are anagrams.")
	else:
	    print("The strings aren't anagrams.") 

# 2.Counter method
from collections import Counter
# function to check if two strings are anagram or not
def check2(s1, s2):
   
	# implementing counter function
	if(Counter(s1) == Counter(s2)):
	    print("The strings are anagrams.")
	else:
	    print("The strings aren't anagrams.")

# 3.sort and list method
def check3():
	x = [inp1[i] for i in range(0,len(inp1))]
	x.sort()
	y = [inp2[i] for i in range(0,len(inp2))]
	y.sort()
	 
	# the sorted strings are checked
	if (x == y):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")

# 4.using a dictionarry
def anagramz(inp1: str, inp2: str) -> bool:
	# if the length of the two strings is not the same, they are not anagrams.
	if len(inp1) != len(inp2):
		return False

	# initialize the dictionary
	counts = {}

	# loop simultaneously through the characters of the two strings.
	for c1, c2 in zip(inp1, inp2):
		if c1 in counts.keys():
		counts[c1] += 1
		else:
		counts[c1] = 1
		if c2 in counts.keys():
		counts[c2] -= 1
		else:
		counts[c2] = -1

	# Loop through the dictionary values.
	# if the dictionary contains even one value which is
	# different than 0, the strings are not anagrams.
	for count in counts.values():
		if count != 0:
		return False
	return True

	# test the implementation
def main():
	inp1 = "listen"
	inp2 = "silent"
	if anagramz(inp1, inp2):
		print(f"{inp1} and {inp2} are anagrams")
	else:
		print(f"{inp1} and {inp2} are not anagrams")

if __name__ == "__main__":
main()

# 5.using count
def check5():
	s1 = "dad"
	s2 = "bad"

	char_list_1 = list(s1)
	char_list_2 = list(s2)

	char_count = {}

	for char in char_list_1:
		if char not in char_count:
			char_count[char] = 0
		char_count[char] += 1

	for char in char_list_2:
		if char not in char_count:
			print("The strings are not anagrams.")
			break
		char_count[char] -= 1

	else:
		for count in char_count.values():
			if count != 0:
				print("The strings are not anagrams.")
				break
		else:
			print("The strings are anagrams.")

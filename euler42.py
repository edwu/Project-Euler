#The goal of this solution was to be as fast as possible and not precompute any of the triangle numbers.
#Therefore this solution should be able to handle any sized word. 
letter_to_value = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
				'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
				'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#prepopulate it with the 1st triangle number
triangle_numbers = [1]

def euler42():
	#number_of_triangle_numbers = 0
	words = open('words.txt').read().replace('"','').split(',')
	number_of_triangle_numbers = len(filter(lambda word: is_triangle_number(value_of_word(word)), words))
	#for word in words:
	#	if is_triangle_number(value_of_word(word)):
	#		number_of_triangle_numbers += 1
	print "Number of triangle numbers:", number_of_triangle_numbers
		
def is_triangle_number(value):
	#Compute triangle numbers as we go, based on what the word value adds up to.
	while (triangle_numbers[-1] < value):
		nth_number_to_compute = len(triangle_numbers) + 1
		triangle_number = nth_triangle_number(nth_number_to_compute)
		triangle_numbers.append(triangle_number)	
	return binary_search(value,0,len(triangle_numbers),triangle_numbers)
	
def nth_triangle_number(n):
 	return int(0.5 * (n * (n+1)))
	
def value_of_word(word):
	return sum(value_of_letter(letter) for letter in word)
	
def value_of_letter(letter):
	return letter_to_value[letter.lower()]
	
def binary_search(input,low,high,sorted_list):
	if low > high:
		return False
	else:	
		mid = (low+high)/2
		if input == sorted_list[mid]:
			return True
		elif input < sorted_list[mid]:
			return binary_search(input,low,mid-1,sorted_list)
		else:
			return binary_search(input,mid+1,high,sorted_list)
	
if __name__ == '__main__':
	euler42()

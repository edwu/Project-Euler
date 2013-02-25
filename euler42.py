#The goal of this solution was to be as fast as possible and not precompute any of the triangle numbers.
#Therefore this solution should be able to handle any sized word.
#prepopulate it with the 1st triangle number
triangle_numbers = [1]


def euler42():
    #number_of_triangle_numbers = 0
    words = open('words.txt').read().replace('"', '').split(',')
    number_of_triangle_numbers = len(filter(lambda word: is_triangle_number(value_of_word(word)), words))
    #for word in words:
    #    if is_triangle_number(value_of_word(word)):
    #        number_of_triangle_numbers += 1
    print "Number of triangle numbers:", number_of_triangle_numbers


def is_triangle_number(value):
    #Compute triangle numbers as we go, based on what the word value adds up to.
    while (triangle_numbers[-1] < value):
        nth_number_to_compute = len(triangle_numbers) + 1
        triangle_number = nth_triangle_number(nth_number_to_compute)
        triangle_numbers.append(triangle_number)
    return binary_search(value, 0, len(triangle_numbers), triangle_numbers)


def nth_triangle_number(n):
    return int(0.5 * (n * (n + 1)))


def value_of_word(word):
    return sum(value_of_letter(letter) for letter in word)


def value_of_letter(letter):
    return ord(letter.lower()) - ord('a') + 1


def binary_search(value, low, high, sorted_list):
    if low > high:
        return False
    else:
        mid = (low + high) / 2
        if value == sorted_list[mid]:
            return True
        elif value < sorted_list[mid]:
            return binary_search(value, low, mid - 1, sorted_list)
        else:
            return binary_search(value, mid + 1, high, sorted_list)

if __name__ == '__main__':
    euler42()

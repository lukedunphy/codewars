# (1) - Even or Odd
def even_or_odd(number):
    pass
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
# # (2) - Convert a Number to a String
def number_to_string(num):
    # Return a string of the number here!
    num = str(num)
    return num

# (3) - Vowel Count
def get_count(sentence):
    pass
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# ----------------------------------    IN     ----------------------------------------
#This funtion return the total number of unique letters in the string using in

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  n_letters = 0
  for i in letters:
    if i in word:
      n_letters += 1
  return n_letters

# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))

# ----------------------------------    SPLIT()     ----------------------------------------
#This funtion return the number of times x appears in word and works when x is 
# multiple characters long.

def count_multi_char_x(word, x):
  split_of_word = word.split(x)
  return len(split_of_word)-1

# Uncomment these function calls to test your function:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1

# ----------------------------------    FIND()     ----------------------------------------
#This funtion return the substring between the first occurrence of start and end in word.
#  If start or end are not in word, the function should return word.

def substring_between_letters(word, start, end):
  word_start = word.find(start)
  word_end = word.find(end)
  if word_start > -1 and word_end > -1:
    return word[word_start+1:word_end]
  return word

# Uncomment these function calls to test your function:
#print(substring_between_letters("aapple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# ----------------------------------    Example #1     ----------------------------------------
#This funtion  return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
    split_sentence = sentence.split(' ')
    for i in split_sentence:
        if len(i) < x:
            return False
    return True
# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True

# ----------------------------------    Example #2   ----------------------------------------
# The function return True if name appears in sentence in all lowercase letters, 
# all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function return False otherwise

# Write your check_for_name function here:


def check_for_name(sentence, name):
  l_sentence = sentence.lower()
  l_name = name.lower()
  split_sentence = l_sentence.split(' ')
  print(split_sentence)
  print(l_name)
  for i in split_sentence:
    if i == l_name:
      return True
  return False

# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#-----------------------------------------------------------------------------
# The function should return a string containing every other letter in word

def every_other_letter(word):
    new_word = ''
    for i in range(0, len(word), 2):
        new_word += (word[i])
    return new_word
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


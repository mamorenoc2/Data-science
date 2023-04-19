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

#This funtion return a array of last names of a string with names authors
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_name = authors.split(',')
author_last_name = []
for name in author_name:
  author_last_name.append(name.split()[-1])

#print(author_last_name)
#should print ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']


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

#another form

def check_for_name_2(sentence, name):
 lower_sentence = sentence.lower()
 lower_name = name.lower()
 split_sentence = lower_sentence.split(lower_name)
 if len(split_sentence)  < 2:
  return False
 return True

# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
#print(check_for_name_2("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
#print(check_for_name_2("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
#print(check_for_name_2("My name is Samantha", "Jamie"))
# should print False

#------------------------------- Example #3 ------------------------------------
# The function should return a string containing every other letter in word

def every_other_letter(word):
    new_word = ''
    for i in range(0, len(word), 2):
        new_word += (word[i])
    return new_word
# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print

#------------------------------- Example #4 ------------------------------------
# The function should return a string containing every other letter in word

def every_other_letter(word):
 every_other_word = ''
 for i in range(0, len(word), 2):
  every_other_word += word[i]
 return every_other_word

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print

#------------------------------- Example #5 ------------------------------------
#The function should return word in reverse

def reverse_string(word):
  reverse_word = ''
  for i in range(len(word)-1, -1, -1):
    reverse_word += word[i]
  return reverse_word


# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print


#------------------------------ Example #6 --------------------------------------

#Finding the first syllable of a word is a difficult task, so for our function,
# we’re going to switch the first letters of each word. Return the two new words 
# as a single string separated by a space.


def make_spoonerism(word1, word2):
  first_letter_of_w1 = word1[0]
  first_letter_of_w2 = word2[0]
  w1_a = word1.replace(word1[0], first_letter_of_w2)
  w2_a = word2.replace(word2[0],first_letter_of_w1)
  return w1_a, w2_a
# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

#------------------------------ Example #7 --------------------------------------

# This function should add exclamation points to the end of word until word is 
# 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  count = 0
  exclamation = ''
  word_m = ''
  if len(word) <= 20:
    while count < len(word):
      exclamation += '!'
      print('Hola' , count)
      count += 1
    word_m = word + exclamation
    return word_m
  return word

# Write your add_exclamation function here:


def add_exclamation(word):
  count = 0
  exclamation = ''
  word_m = ''
  if len(word) <= 20:
    while count < len(word):
      exclamation += '!'
      print('Hola' , count)
      count += 1
    word_m = word + exclamation
    return word_m
  return word

# Uncomment these function calls to test your function:
#print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# Question-10
# parameter datatype is string, return datatype is boolean
def is_palindrome(word):
    reverse_word = ''
    for i in range(len(word) - 1, -1, -1):
        reverse_word = reverse_word + word[i]
    if reverse_word == word:
        return True
    else:
        return False

print(is_palindrome('mom'))

letter = "abc"
print(letter[0])








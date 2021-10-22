# Question-7
# parameter datatype is string, return datatype is string
def replace_with_A(word):
    s = ''
    for i in range(0, len(word)):# 0-4
        if word[i].islower():
            s = s + 'A'# s = ANNAA,
        else:
            s = s + word[i]# s = ANNAA
    return s

print(replace_with_A('aNNaa'))

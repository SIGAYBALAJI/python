'''def reverse(str):
    return str[::-1]
str='Hello World!'
print(reverse(str))'''
def reverse(s):
    word=s.split()
    print(word)
    reversed_word=" ".join(reversed(word))
    return reversed_word
s='Hello,World!'
print(reverse(s))

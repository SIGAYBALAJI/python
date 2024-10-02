def palindromecheck(s):
    return s==s[::-1]
str='madam'
if palindromecheck(str):
    print("1")
else:
    print("0")
    

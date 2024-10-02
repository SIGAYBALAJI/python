#Method 1
'''def is_palindrome(s):
    return s==s[::-1]
def is_symetric(s):
    length=len(s)
    mid=length//2
    if length%2==0:
        return s[:mid]==s[mid:]
    else:
        return s[:mid]==s[mid+1:]
s="amaama"
if is_palindrome(s):
    print("the entered string is palindrome")
else:
    print("the entered string is not  palindrome")
if is_symetric(s):
    print("the entered string is symetric")
else:
    print("the entered string is not a symetric")'''
#Method 2
def is_palindrome(s):
    return s==s[::-1]
def is_symetric(s):
    mid=len(s)//2
    return s[:mid]==s[-mid:]
s="amaama"
if is_palindrome(s):
    print("the entered string is palindrome")
else:
    print("the entered string is not  palindrome")
if is_symetric(s):
    print("the entered string is symetric")
else:
    print("the entered string is not a symetric")


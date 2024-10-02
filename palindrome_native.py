def ispalindrome(s):
    return s==s[::-1]
s=input()
res=ispalindrome(s)
if res:
    print("yes")
else:
    print("No")

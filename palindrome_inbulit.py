def ispalindrome(s):
    rev="".join(reversed(s))
    if(s==rev):
        return True
    return False
s=input()
res=ispalindrome(s)
if res:
    print("yes")
else:
    print("No")

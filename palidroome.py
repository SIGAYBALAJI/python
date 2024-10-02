#Method 1
'''def ispalindrome(s):
    return s==s[::-1]
s='dad'
res=ispalindrome(s)
if res:
    print("Yes")
else:
    print("No")'''
   
#Method 2
'''def ispalindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return False
        else:
            return True
s='malayalam'
res=ispalindrome(s)
if res:
    print("yes")
else:
    print("No")'''
#Method 3
def ispalindrome(s):
    rev='  ' . join(reversed(s))
    if(s == rev):
        return True
    return False
s='malayalam'
res=ispalindrome(s)
if res:
    print("Yes")
else:
    print("No")
                   

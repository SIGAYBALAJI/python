def ispalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] !=str[len(str)-i-1]:
            return False
    return True
s="malayalam"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")

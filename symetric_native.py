def symetric(s):
    length=len(s)
    mid=length//2
    if length%2==0:
        return s[:mid]==s[mid:]
    else:
        return s[:mid]==s[mid+1:]
s=input()
res=symetric(s)
if res:
    print(f"string is {s} is symetric")
else:
    print(f"string is {s} is symetric")

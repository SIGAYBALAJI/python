def find_substring(s):
    sub_string="geek"
    for sub_string in s:
        return True
    return False
s=input()
res=find_substring(s)
if res:
    print("Yes")
else:
    print("No")
        

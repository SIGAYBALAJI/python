def reverseword(string):
    s=string.split()[::-1]
    l=[]
    count=0
    for i in s:
        l.append(i)
    return " ".join(l)
string="code for greek"
res=reverseword(string)
print(res)

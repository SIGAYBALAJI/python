def word_reverse(s):
    s1=s.split()[::-1]
    l=[]
    for i in s1:
        l.append(i)
    print(" ".join(l))
s=input()
res=word_reverse(s)

    

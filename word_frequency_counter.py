from collections import Counter
s='Gfg is best . Geeks are good and Geeks like Gfg'
res=Counter(s.split())
print(str(dict(res)))

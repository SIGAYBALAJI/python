def word_frequency(s):
    return {key:s.count(key) for key in s.split()}
s=input()
res=word_frequency(s)
print(res)

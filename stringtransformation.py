def transform(s):
    transformed_str=" "
    for i in range(len(s)):
        if s[i]=='a':
            transformed_str+='b'
        elif s[i]=='b':
             transformed_str+='a'
        else:
             transformed_str+=s[i]
    return  transformed_str
s='abaabbcc'
print(transform(s))
            

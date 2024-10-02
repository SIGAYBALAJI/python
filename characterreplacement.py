def characterreplacement(str):
    replacedcharacter=" "
    for i in range(len(str)):
        if str[i]=='a':
            replacedcharacter+='p'
            
        elif str[i]=='p':
               replacedcharacter+='a'
        else:
           replacedcharacter+=str[i]
    return replacedcharacter
str='apples'
print(characterreplacement(str))

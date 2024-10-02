from collections import Counter
str="swiss"
char_count=Counter(str)
for char in str:
    if char_count[char]==1:
        print(char)
        break

str='syncfusion'
n=len(str)
count=0
word=" "
for i in range(n):
    if count==4:
        print(word)
        count=1
        word=" "
    else:
        count=count+1
    word=word+str[i]

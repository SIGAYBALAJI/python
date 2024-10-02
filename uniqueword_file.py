with open("destination.txt","r") as file:
    content=file.read()
    unique_word=sorted(set(content.lower().split()))
with open("unique.txt","w") as file1:
    for word in unique_word:
        file1.write(word)
        file1.write('\n')

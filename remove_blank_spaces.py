with open("destination.txt","r") as file:
    content=file.readlines()
    print(content)
with open("destination.txt","w") as file1:
    for line in content:
        if line.strip():
            file1.write(line)

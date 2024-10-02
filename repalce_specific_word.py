with open("unique.txt","r") as file:
   content= file.read()
content=content.replace("balaji","rajesh")
with open("unique.txt","w") as file1:
    file1.write(content)

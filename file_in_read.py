with open("demo.txt",'r') as file:
    with open("demo1.txt",'w') as file1:
        for line in file.readlines():
            if not(line.startswith("my")):
                print(line)
                file1.write(line)
file1.close()
file.close()
         
    
   


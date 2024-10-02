#f=open("firstfile.txt",'r')
#print(f.read())
'''f=open("firstfile.txt",'w')
f.write("python is amazing language")
f.close()'''
'''f=open("firstfile.txt",'a')
f.write("i'm append the data ")'''
'''f=open("firstfile.txt",'w')
print(f.write("hii"))'''
f1=open("firstfile.txt",'r')
f2=open("secondfile.txt",'w')
for i in f1:
    print(f2.write(i))
f2.close()    



input_file=["file1.txt","file2.txt","merged.txt"]
with open("mergedf.txt","w") as outfile:
    for file in input_file:
        with open(file,'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n')

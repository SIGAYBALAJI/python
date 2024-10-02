lst=[[1,2,3],
        [4,5,6],
        [7,8,9]]
transpose=[ list(i) for i in zip(*lst)]
print(transpose)

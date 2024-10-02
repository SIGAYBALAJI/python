def iseven(num):
    return not num&1
if __name__ == "__main__":
    num=8
    if iseven(num):
        print("even")
    else:
        print("odd")


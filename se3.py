"""Sequence I"""
def main(num):
    """see loop"""
    for j in range(num):
        for i in range(1, num+1):
            print("%d"%(i + j*num), end=" ")
        print("")
main(int(input()))

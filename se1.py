"""Sequence I"""
def main(num):
    """see loop"""
    for _ in range(num):
        for i in range(1, num+1):
            print("%d"%(i), end=" ")
        print("")
main(int(input()))

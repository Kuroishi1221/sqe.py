"""Sequence VII"""
def main(num):
    """see loop"""
    for i in range(1, num + 1):
        print("   "*(num - i), end="")
        for j in range(i):
            print("%02d"%(j + 1), end=" ")
        for j in range(i - 1):
            print("%02d"%(i - j - 1), end=" ")
        print("")
main(int(input()))

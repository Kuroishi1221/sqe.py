"""Sequence VII"""
def main(num):
    """see loop"""
    for i in range(1, num + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print("")
    for i in range(num - 1):
        for j in range((num - 1) - i):
            print(j + 1, end=" ")
        print("")
#1 2 3 4 5 6
main(int(input()))

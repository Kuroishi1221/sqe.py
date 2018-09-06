"""Sequence I"""
def main(num):
    """see loop"""
    count = 0
    for i  in range(num, 0, -1):
        if count < 6:
            print(i, end=" ")
        else:
            print(i)
            count = -1
        count += 1
main(int(input()))

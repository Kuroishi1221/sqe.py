"""se2"""
def main():
    """main function"""
    num = int(input())
    collect = 1
    print(collect, end=" ")
    for i in range(num - 1):
        collect += 3 + (2* i)
        print(collect, end=" ")
main()

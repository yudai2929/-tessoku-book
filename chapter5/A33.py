import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    A = LI()

    sum_xor = 0
    for a in A:
        sum_xor ^= a

    if sum_xor == 0:
        print("Second")
    else:
        print("First")


if __name__ == "__main__":
    main()

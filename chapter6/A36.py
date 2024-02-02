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
    N, K = LI()

    if K < 2 * (N - 1):
        print("No")
        return

    if N % 2 == 0 and K % 2 == 0:
        print("Yes")
        return

    if N % 2 == 1 and K % 2 == 0:
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()

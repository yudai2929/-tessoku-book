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

    a = N // 3
    b = N // 5
    c = N // 15

    ans = a + b - c
    print(ans)


if __name__ == "__main__":
    main()

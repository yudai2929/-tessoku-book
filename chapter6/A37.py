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
    N, M, B = LI()
    A = LI()
    C = LI()

    A_sum = sum(A)
    C_sum = sum(C)

    ans = A_sum * M + C_sum * N + B * N * M

    print(ans)


if __name__ == "__main__":
    main()

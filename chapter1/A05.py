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

    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            k = K - i - j
            if 1 <= k <= N:
                count += 1

    print(count)


if __name__ == "__main__":
    main()

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
    N, A, B = LI()

    dp = [False for _ in range(N + 1)]

    for i in range(N + 1):
        if i - A >= 0 and dp[i - A] == False:
            dp[i] = True
        if i - B >= 0 and dp[i - B] == False:
            dp[i] = True

    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
